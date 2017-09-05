"""main.py"""

import sys
import os
import json

from xcmodelcreate import Model

from pbxproj import XcodeProject as xc

def runwithargs(args):
    """Start writing models into xcode project"""

    # Init Variables
    models_json = json.loads(args[0])
    project_name = args[1]
    model_folder = args[2]

    project = xc.load('%s.xcodeproj/project.pbxproj' % (project_name))
    backup = project.backup()

    def createmodel(model_name, model_json):
        """Creates a model based on a type name and a json containing properties"""

        model_path = "%s/%s.swift" % (model_folder, model_name)

        print "Preparing to edit project ...\nBackup file = %s" % (backup)
        project.add_file('%s/%s.swift' % (model_folder, model_name), force=False)
        project.save()

        swift_str = Model(model_name, model_json).swift_implementation
        print swift_str

        model_file = open(model_path, "w")
        model_file.write(swift_str)
        model_file.close()

    for key in models_json.keys():
        model_json = models_json[key]
        createmodel(key, model_json)

    print "--- Writing to files finished with success! ---"
    print "--- Cleaning up ... ---"
    try:
        os.remove(backup)
    except OSError:
        pass
    print "--- Done ---"

def validate(args):
    """
    Validates the given inputs. Takes one string array \"args\"
        arguments:
        - args: An array of inputs
    """

    arg_names = ["models_json", "project_name", "model_folder"]
    valid = True
    print args
    if len(args) < 3:
        valid = None
        i = len(args)
        while i < 3:
            print "Missing input for %s" % (arg_names[i])
            i += 1
    elif len(args) > 4:
        valid = None
        print "Too many arguments! Arguments are:"
        for idx, element in enumerate(arg_names):
            print "args[%d] = %s" % (idx, element)
    return valid

def main():
    """The main function of the applications"""

    print """
--- www.DeveloThor.codes ---

--- validating inputs ... ---
"""

    args = sys.argv
    del args[0]
    if validate(sys.argv):
        runwithargs(sys.argv)
    else:
        sys.exit(-1)
