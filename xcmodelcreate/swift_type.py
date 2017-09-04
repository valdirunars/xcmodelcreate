"""swift_type.py"""

def supported_types():
    """Swift's Foundation types currently being supported"""

    return [
        "String",
        "Bool",
        "Date",
        "Double",
        "Float",
        "Float64",
        "Float32",
        "Float16",
        "Float8",
        "Int",
        "Int64",
        "Int32",
        "Int16",
        "Int8",
        "UInt",
        "UInt64",
        "UInt32",
        "UInt16",
        "UInt8"
    ]

class SwiftType(object):
    """Contains info for a supported Swift type."""

    swift_type = "<#Some Type#>"
    is_optional = False

    def is_custom_type:
        return self.swift_type in supported_types()

    def __init__(self, string):
        last_index = len(string) - 1

        self.swift_type = string
        self.is_optional = string[last_index] == "?"
