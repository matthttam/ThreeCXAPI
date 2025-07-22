import yaml
import inspect
import re
import keyword
import builtins
import threecxapi.components.schemas.pbx as pbx_module


def extract_enum_definitions(yaml_file_path: str) -> dict[str, list[str]]:
    with open(yaml_file_path, "r") as f:
        data = yaml.safe_load(f)

    schemas = data.get("components", {}).get("schemas", {})
    enum_definitions = {}

    for name, definition in schemas.items():
        enum_values = definition.get("enum")
        if enum_values:
            clean_name = name.removeprefix("Pbx.")
            enum_definitions[clean_name] = enum_values

    return enum_definitions


def extract_object_schemas(yaml_file_path: str) -> dict[str, dict]:
    with open(yaml_file_path, "r") as f:
        data = yaml.safe_load(f)

    schemas = data.get("components", {}).get("schemas", {})
    object_definitions = {}

    for name, definition in schemas.items():
        if isinstance(definition, dict) and definition.get("type") == "object":
            clean_name = name.removeprefix("Pbx.")
            object_definitions[clean_name] = definition

    return object_definitions


def get_schema_class_fields(module) -> dict[str, list[str]]:
    classes = {}
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and obj.__module__ == module.__name__:
            classes[name] = list(obj.__annotations__.keys())
    return classes


def to_snake_case(name: str) -> str:
    name = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


def map_openapi_type(schema: dict) -> str:
    type_ = schema.get("type")
    nullable = schema.get("nullable", False)

    if "$ref" in schema:
        ref = schema["$ref"].split("/")[-1]
        result = ref.split(".")[-1]
    elif type_ == "string":
        result = "str"
    elif type_ == "integer":
        result = "int"
    elif type_ == "number":
        result = "float"
    elif type_ == "boolean":
        result = "bool"
    elif type_ == "array":
        items = schema.get("items", {})
        inner_type = map_openapi_type(items)
        result = f"list[{inner_type}]"
    elif type_ == "object":
        result = "dict"
    else:
        result = "Any"

    return f"Optional[{result}]" if nullable or type_ == "array" else result


def sort_missing_classes(missing: set[str], swagger_objects: dict) -> list[str]:
    def normalize_name(name: str) -> str:
        if name.startswith("Pbx."):
            return name[len("Pbx.") :]
        return name

    sorted_list = []
    seen = set()
    remaining = set(missing)

    def extract_refs(obj: dict) -> set[str]:
        refs = set()

        def recurse_extract(o):
            if isinstance(o, dict):
                if "$ref" in o:
                    ref_name = o["$ref"].split("/")[-1]
                    refs.add(normalize_name(ref_name))
                else:
                    for v in o.values():
                        recurse_extract(v)
            elif isinstance(o, list):
                for item in o:
                    recurse_extract(item)

        all_of = obj.get("allOf", [])
        recurse_extract(all_of)
        properties = obj.get("properties", {})
        recurse_extract(properties)

        return refs

    while remaining:
        progress = False
        for name in sorted(remaining):  # Deterministic order
            definition = swagger_objects.get(name, {})
            refs = extract_refs(definition)

            unresolved_refs = {ref for ref in refs if ref in remaining}

            if not unresolved_refs:
                sorted_list.append(name)
                seen.add(name)
                remaining.remove(name)
                progress = True
                break  # Restart outer loop for stability

        if not progress:
            # No progress made — break potential cycles
            for name in sorted(remaining):
                sorted_list.append(name)
            break

    return sorted_list


if __name__ == "__main__":
    file_path = "./openapi/openapi_3.0.4.yml"
    swagger_objects = extract_object_schemas(file_path)
    swagger_enums = extract_enum_definitions(file_path)
    python_classes = get_schema_class_fields(pbx_module)

    swagger_object_names = set(swagger_objects.keys())
    swagger_enum_names = set(swagger_enums.keys())
    python_class_names = set(python_classes.keys())

    missing_in_python = swagger_object_names - python_class_names
    extra_in_python = python_class_names - swagger_object_names
    sorted_missing = sort_missing_classes(missing_in_python, swagger_objects)

    print("# === Missing in Python ===")
    for name in sorted_missing:
        definition = swagger_objects[name]
        class_name = name.split(".")[-1]

        # Handle 'allOf' at the top level of the object
        all_of = definition.get("allOf")
        if all_of:
            # Gather base classes from $ref
            base_classes = []
            props = {}
            required = set()

            for entry in all_of:
                if "$ref" in entry:
                    ref = entry["$ref"]
                    ref_name = ref.split("/")[-1].split(".")[-1]
                    base_classes.append(ref_name)
                elif entry.get("type") == "object":
                    props.update(entry.get("properties", {}))
                    required.update(entry.get("required", []))

            bases = ", ".join(base_classes) if base_classes else "BaseModel"
        else:
            props = definition.get("properties", {})
            required = set(definition.get("required", []))
            bases = "Schema"

        print(f"\nclass {class_name}({bases}):")
        if not props:
            print("    pass")
            continue

        for prop_name, prop_schema in props.items():
            # Handle allOf at the property level
            if "allOf" in prop_schema:
                merged_schema = {}
                for part in prop_schema["allOf"]:
                    if "$ref" in part:
                        merged_schema = part  # Use ref directly
                        break
                    elif "type" in part or "properties" in part:
                        merged_schema.update(part)
                prop_schema = merged_schema

            if "oneOf" in prop_schema:
                union_types = []
                for variant in prop_schema["oneOf"]:
                    is_nullable = variant.get("nullable", False)
                    type_str = map_openapi_type(variant)
                    union_types.append(type_str)

                # Remove duplicates but preserve order
                seen = set()
                unique_union = []
                for t in union_types:
                    if t not in seen:
                        seen.add(t)
                        unique_union.append(t)

                type_hint = " | ".join(unique_union)
                # type_hint = union_str if is_required else f"Optional[{union_str}]"

            else:
                type_hint = map_openapi_type(prop_schema)

            is_required = prop_name in required

            # Determine final property name and alias
            banned_names = set(keyword.kwlist) | set(dir(builtins)) | {"Optional", "Field", "Schema", "BaseModel"}
            if prop_name.startswith("@"):
                final_name = prop_name.split(".")[-1]
                alias_snippet = f', alias="{prop_name}"'
            elif prop_name in banned_names:
                final_name = to_snake_case(prop_name)
                alias_snippet = f', alias="{prop_name}"'
            elif prop_name in swagger_enum_names or f"Pbx.{prop_name}" in swagger_object_names or prop_name in swagger_object_names:
                final_name = to_snake_case(prop_name)
                alias_snippet = f', alias="{prop_name}"' if final_name != prop_name else ""
            else:
                final_name = prop_name
                alias_snippet = ""

            # Print the field
            if type_hint.startswith("Optional[list"):
                print(f"    {final_name}: {type_hint} = Field(default=None{alias_snippet})")
            elif type_hint.startswith("Optional["):
                print(f"    {final_name}: {type_hint} = Field(default=None{alias_snippet})")
            elif is_required:
                print(f"    {final_name}: {type_hint} = Field(...{alias_snippet})")
            else:
                print(f"    {final_name}: {type_hint} = Field(default=None{alias_snippet})")

    # print("\n=== Extra in Python ===")
    # for name in sorted(extra_in_python):
    #    print(name)

    # print("\n=== Differences in Properties ===")
    # for obj_name in sorted(swagger_object_names & python_class_names):
    #    swagger_props = set(swagger_objects[obj_name])
    #    python_props = set(python_classes[obj_name])
#
#    missing_props = swagger_props - python_props
#    extra_props = python_props - swagger_props
#
#    if missing_props or extra_props:
#        print(f"\nIn object '{obj_name}':")
#        if missing_props:
#            print("  Missing properties:")
#            for prop in sorted(missing_props):
#                print(f"    {prop}")
#        if extra_props:
#            print("  Extra properties:")
#            for prop in sorted(extra_props):
#                print(f"    {prop}")
