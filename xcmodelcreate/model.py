# -*- coding: utf-8 -*-
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

        tmp_prop_string = "\n\t".join(map(extract_declaration, self.properties))
        prop_string = "\t%s" % (tmp_prop_string)
        coding_keys_cases = "\n\t\t".join(map(extract_coding_key_case, self.properties))
        coding_keys = "\tprivate enum CodingKeys: String, CodingKey {\n\t\t%s\n\t}" % (coding_keys_cases)
        i_f = "import Foundation"

        self.swift_implementation = "%s\n\nstruct %s: Codable, Decodable {\n%s\n\n%s\n}" % (i_f, name, prop_string, coding_keys)
        self.name = name
