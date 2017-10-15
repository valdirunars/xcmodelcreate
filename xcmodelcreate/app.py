# -*- coding: utf-8 -*-
"""main.py"""

import sys
import os

from xcmodelcreate import model_creator
from xcmodelcreate import validator
from xcmodelcreate import constants

def initialize():
    """The initialization method for `xcmodelcreate init`"""

    if not os.path.exists(constants.FOLDER_PATH):
        os.makedirs(constants.FOLDER_PATH)
    else:
        print "--- Already initialized ---"
        exit(1)

    config = open("%s/config.json" % (constants.FOLDER_PATH), 'a')

    project_arr = os.system('ls *.xcodeproj')
    if len(project_arr) <= 0:
        print "No *.xcodeproj found"
        sys.exit(-1)
    xcproject_path = project_arr[0]

    json_path = "%s/models.json" % (constants.FOLDER_PATH)
    models_path = "Sources/Models"
    group_path = "Sources/Models"

    json = """
{
    \"json_path\": \"%s\",
    \"xcodeproj\":\"%s\",
    \"model_group\": \"%s\",
    \"model_folder\": \"%s\"
}
    """ % (json_path, xcproject_path, group_path, models_path)
    config.write(json)

    models = open("%s/models.json" % (constants.FOLDER_PATH), 'a')
    models.write("{}")


def main():
    """The main function of the applications"""

    print "---  © Thorvaldur Runarsson  ---"
    print "--- \"github.com/valdirunars\""
    print "     validating inputs ... ---"

    # extract arguments
    args = sys.argv

    # clear first argument which is always something like "/usr/local/bin/xcmodelcreate"
    del args[0]

    # first element is the "method" being called
    method = args[0]

    del args[0]

    print("method = " + method)
    validator.validate_method(method)

    validator.validate(args, method)

    if method == constants.METHOD_ALL:
        model_creator.create_models()
    elif method == constants.METHOD_INIT:
        initialize()
    else:
        print "--- Error: Invalid method: \"%s\" ---" % (method)
        sys.exit(-1)
