"""validator.py"""
import constants

def validate_method(method):
    return method.lower() in VALID_METHODS

def validate(args, method):
    """
    Validates the given inputs. Takes one string array \"args\"
        arguments:
        - args: An array of inputs
    """

    if method == "init" || method == "all":
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
    return valid
