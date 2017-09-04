"""model.py"""

from xcmodelcreate import SwiftProperty

def extract_declaration(swift_property):
    """E.g. for SwiftProperty("SomeModel", "{ 'some': 'String' }") returns \"let some: String\""""
    return swift_property.declaration

def extract_coding_key_case(swift_property):
    """E.g. for SwiftProperty("SomeModel", "{ 'some': 'String' }") returns \"case some\""""
    return "case %s" % (swift_property.property_name)

class Model(object):
    """Info wrapper that represents a Swift Model"""

    properties = []
    swift_implementation = None
    name = None

    def __init__(self, name, jsonDic):
        for key in jsonDic:
            value = jsonDic[key]
            self.properties.append(SwiftProperty(key, value))

        prop_string = "\n\t".join(map(extract_declaration, self.properties))
        coding_keys_cases = "\n\t\t".join(map(extract_coding_key_case, self.properties))
        coding_keys = "\tCodingKeys {\n\t\t%s\n\t}" % (coding_keys_cases)
        i_f = "import Foundation"

        self.swift_implementation = "%s\n\n%s {\n%s\n\n%s\n}" % (i_f, name, prop_string, coding_keys)
        self.name = name
