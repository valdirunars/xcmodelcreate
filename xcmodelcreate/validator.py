# -*- coding: utf-8 -*-
"""validator.py"""
import constants
import sys

def validate_method(method):
    if (method.lower() in constants.VALID_METHODS) == False:
        print "--- Error: Invalid method: \"%s\" ---" % (method)
        sys.exit(-1)

def validate(args, method):
    """
    Validates the given inputs. Takes one string array \"args\"
        arguments:
        - args: An array of inputs
    """

    if method in [constants.METHOD_INIT, constants.METHOD_ALL]:
        arg_names = []
    elif method == "raw":
        arg_names = [
            "models_json",
            "model_folder",
            "model_group"
        ]

    valid = True
    print args

    valid_arg_count = len(arg_names)

    if len(args) < valid_arg_count:
        valid = None
        i = len(args)
        while i < valid_arg_count:
            print "Missing input for %s" % (arg_names[i])
            i += 1
    elif len(args) > valid_arg_count:
        valid = None
        print "Too many arguments! Arguments are:"
        for idx, element in enumerate(arg_names):
            print "args[%d] = %s" % (idx, element)
    if valid == None:
        sys.exit(-1)
