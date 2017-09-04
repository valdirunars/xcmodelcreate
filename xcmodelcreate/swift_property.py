"""swift_property.py"""

from xcmodelcreate import SwiftType

class SwiftProperty(object):
    """Info wrapper around a single Swift property"""

    property_name = "<#Some struct#>"
    token = None
    declaration = None

    def __init__(self, key, value):
        self.property_name = key
        self.token = SwiftType(value)
        self.declaration = "let %s: %s" % (self.property_name, self.token.swift_type)
