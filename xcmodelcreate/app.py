"""main.py"""

import sys
import os
from xcmodelcreate import model_creator
from xcmodelcreate import validator
from xcmodelcreate import constants

def main():
    """The main function of the applications"""

    print "--- www.DeveloThor.codes ---"
    print "--- validating inputs ... ---"

    args = sys.argv

    # first argument is always app.py because python is the actual command
    del args[0]

    if validator.validate(sys.argv):
        element_list = os.listdir(".")
        project_name = None
        for element in element_list:
            if element.endswith(DOT_XCODEPROJ):
                project_name = element.split(DOT_XCODEPROJ)[0]
                break
        if project_name == None:
            print "--- Error: Couldn't find an xcodeproj at the root level of the current directory---"
            sys.exit(-1)

        project_name =
        model_creator.create_models(sys.argv, project_name)
    else:
        sys.exit(-1)
