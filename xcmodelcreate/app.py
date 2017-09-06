"""main.py"""

import sys
import os
from xcmodelcreate import model_creator
from xcmodelcreate import validator
from xcmodelcreate import constants

def initialize():
    print "--- Calling unimplemented method: init ---"

def main():
    """The main function of the applications"""

    print "--- www.DeveloThor.codes ---"
    print "--- validating inputs ... ---"

    # check for a xcode project
    element_list = os.listdir(".")
    project_name = None
    for element in element_list:
        if element.endswith(DOT_XCODEPROJ):
            project_name = element.split(DOT_XCODEPROJ)[0]
            break

    # extract arguments
    args = sys.argv

    # first element is the "method" being called
    method = args[0]

    if validator.validate_method(method) == False:
        print "--- Error: Invalid method: \"%s\" ---" % (method)
        sys.exit(-1)
    if project_name == None:
        print "--- Error: Couldn't find an xcodeproj at the root level of the current directory ---"
        sys.exit(-1)

    # remove method from array also so arguments ar
    del args[0]

    if validator.validate(args, method):
        if method == METHOD_ALL || method == METHOD_RAW:
            model_creator.create_models(args, project_name)
        elif method == METHOD_INIT:
            initialize()
        else:
            print "--- Error: Invalid method: \"%s\" ---" % (method)
    else:
        sys.exit(-1)
