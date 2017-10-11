# -*- coding: utf-8 -*-
"""swift_type.py"""
from xcmodelcreate import constants

class SwiftType(object):
    """Contains info for a supported Swift type."""

    swift_type = "<#Some Type#>"
    is_optional = False
    is_custom_type = True

    def __init__(self, string):
        last_index = len(string) - 1

        self.is_custom_type = string in constants.SUPPORTED_TYPES
        self.swift_type = string
        self.is_optional = string[last_index] == "?"
