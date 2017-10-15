# -*- coding: utf-8 -*-
"""validator.py"""
import sys
from xcmodelcreate import constants

def validate_method(method):
    """ Method for validating argument inputs """
    if (method.lower() in constants.VALID_METHODS) is False:
        print "--- Error: Invalid method: \"%s\" ---" % method
        sys.exit(-1)
