import yaml
import inspect
import re
import keyword
import builtins
from typing import Union
from collections import OrderedDict

banned_names = set(keyword.kwlist) | set(dir(builtins)) | {"Optional", "Field", "Schema", "BaseModel"}


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
            # Skip any that contain a dot in the name as they don't belong in the Pbx namespace itself
            if "." in clean_name:
                continue
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
    format_ = schema.get("format")
    # nullable = schema.get("nullable", False)
    allOf = schema.get("allOf", [])
    if allOf:
        # Handle 'allOf' by merging schemas
        merged_schema = {}
        for part in allOf:
            if "$ref" in part:
                schema["$ref"] = part["$ref"]
                # merged_schema = pbx_module.__dict__.get(ref_name, {})
            else:
                merged_schema.update(part)

    elif "$ref" in schema:
        ref = schema["$ref"].split("/")[-1]
        result = ref.split(".")[-1]
    elif type_ == "string":
        if format_ == "uuid":
            result = "UUID"
        elif format_ == "date-time":
            result = "datetime"
        else:
            result = "str"
    elif type_ == "integer":
        if format_ == "decimal":
            result = "Decimal"
        else:
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

    # return f"Optional[{result}]" if nullable or type_ == "array" else result
    return result


def sort_swagger_objects(swagger_objects: dict) -> list[str]:
    def normalize_name(name: str) -> str:
        if name.startswith("Pbx."):
            return name[len("Pbx.") :]
        return name

    ordered_dict = OrderedDict()
    seen = set()
    keys_remaining = sorted(set(swagger_objects.keys()))

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

    while keys_remaining:
        progress = False
        for key in keys_remaining:  # Deterministic order
            definition = swagger_objects.get(key, {})
            refs = extract_refs(definition)

            unresolved_refs = {ref for ref in refs if ref in keys_remaining}

            if not unresolved_refs:
                ordered_dict[key] = definition
                seen.add(key)
                keys_remaining.remove(key)
                progress = True
                break  # Restart outer loop for stability

        if not progress:
            # No progress made — break potential cycles
            for key in keys_remaining:
                ordered_dict[key] = definition
            break

    return ordered_dict


import re


def convert_ref_to_class_name(ref: str) -> str:
    pattern = r".*[./]([^./]+)$"
    match = re.search(pattern, ref)
    if match:
        return match.group(1)


def parse_swagger_object_to_python(swagger_object_key, swagger_object: dict) -> str:
    global banned_names
    python_code = ""
    properties = {}
    banned_names.add(swagger_object_key)

    # Handle 'allOf' at the top level of the object
    all_of = swagger_object.get("allOf")
    if all_of:
        # Gather base classes from $ref
        base_classes = []
        for entry in all_of:
            if "$ref" in entry:
                ref = entry["$ref"]
                base_classes.append(convert_ref_to_class_name(ref))
            elif entry.get("type") == "object":
                properties.update(entry.get("properties", {}))

        bases = ", ".join(base_classes) if base_classes else "Schema"
    else:
        properties = swagger_object.get("properties", {})
        bases = "Schema"

    python_code += f"class {swagger_object_key}({bases}):"
    if properties:
        python_code += parse_swagger_object_property_to_python(properties)
    else:
        python_code += "    pass"
    return python_code


def parse_swagger_object_property_to_python(properties: dict) -> str:
    python_code = ""

    for prop_name, prop_schema in properties.items():
        optional = prop_schema.get("nullable", False)
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
                # For python if any of the options are nullable then the entire field is nullable.
                if not optional:
                    optional = variant.get("nullable", False)
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

        if optional:
            type_hint = f"Optional[{type_hint}]"
        # Determine final property name and alias
        if prop_name.startswith("@"):
            final_name = prop_name.split(".")[-1]
            alias_snippet = f', alias="{prop_name}"'
        elif prop_name in banned_names:
            final_name = to_snake_case(prop_name)
            alias_snippet = f', alias="{prop_name}"'
        # elif prop_name in swagger_enum_names or f"Pbx.{prop_name}" in swagger_object_names or prop_name in swagger_object_names:
        #     final_name = to_snake_case(prop_name)
        #     alias_snippet = f', alias="{prop_name}"' if final_name != prop_name else ""
        else:
            final_name = prop_name
            alias_snippet = ""

        if optional:
            default_snippet = "default=None"
        else:
            default_snippet = "..."
        python_code += f"\n    {final_name}: {type_hint} = Field({default_snippet}{alias_snippet})"

    return python_code


if __name__ == "__main__":
    file_path = "./.openapi/openapi_3.0.4.yml"
    swagger_objects = extract_object_schemas(file_path)
    swagger_enums = extract_enum_definitions(file_path)

    swagger_object_names = set(swagger_objects.keys())
    swagger_enum_names = set(swagger_enums.keys())

    banned_names.update(swagger_enum_names)

    sorted_swagger_objects = sort_swagger_objects(swagger_objects)

    python_code = ""
    for swagger_object_key, swagger_object in sorted_swagger_objects.items():
        # if(swagger_object.get("type") == "object" and swagger_object_key not in swagger_enum_names):
        python_code += parse_swagger_object_to_python(swagger_object_key, swagger_object)
        python_code += f"\n\n\n"
    print(python_code)
