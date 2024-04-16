from enum import StrEnum, EnumMeta


class TcxStrEnumMeta(EnumMeta):
    # StrEnum from 3CX can contain teh word None which we can't use in Python
    # So, we use NONE instead. This metaclass makes it so looking for None
    # returns the value for NONE instead.
    def __getitem__(self, name):
        if name == "None":
            name = "NONE"
        if name == "-INF":
            name = "NEGATIVE_INF"
        return super().__getitem__(name).value


class TcxStrEnum(StrEnum, metaclass=TcxStrEnumMeta):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        if name == "NONE":
            return "None"
        if name == "NEGATIVE_INF":
            name = "-INF"
        return name
