# -*- coding: utf-8 -*-
"""main.py"""

import sys
import os
from xcmodelcreate import model_creator
from xcmodelcreate import validator
from xcmodelcreate import constants

def initialize():
    if not os.path.exists(constants.FOLDER_PATH):
        os.makedirs(constants.FOLDER_PATH)
    else:
        print "--- Already initialized ---"
        exit(1)

    config = open("%s/config.json" % (constants.FOLDER_PATH), 'a')
    json_path = "%s/models.json" % (constants.FOLDER_PATH)
    models_path = "Sources/Models"
    group_path = "Sources/Models"
    config.write("{\n\t\"json_path\": \"%s\",\n\t\"model_group\": \"%s\",\n\t\"model_folder\": \"%s\"\n}" % (json_path, group_path, models_path))

    models = open("%s/models.json" % (constants.FOLDER_PATH), 'a')
    models.write("{}")


def main():
    """The main function of the applications"""

    print "--- www.DeveloThor.codes ---"
    print "--- validating inputs ... ---"

    # check for a xcode project
    element_list = os.listdir(".")
    project_name = None
    for element in element_list:
        if element.endswith(constants.DOT_XCODEPROJ):
            project_name = element.split(constants.DOT_XCODEPROJ)[0]
            break


    # extract arguments
    args = sys.argv

    # clear first argument which is always something like "/usr/local/bin/xcmodelcreate"
    del args[0]

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
        if method in [constants.METHOD_ALL, constants.METHOD_RAW]:
            model_creator.create_models(args, project_name, method)
        elif method == constants.METHOD_INIT:
            initialize()
        else:
            print "--- Error: Invalid method: \"%s\" ---" % (method)
    else:
        sys.exit(-1)
