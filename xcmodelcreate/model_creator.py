"""model_creator.py"""
import os
import json
from xcmodelcreate import Model
from pbxproj import XcodeProject as xc

class ModelCreator(object):
    """A structure around creating a Swift model"""

    project = None
    backup = None

    def __init__(self, project_name):
        proj = xc.load('%s.xcodeproj/project.pbxproj' % (project_name))
        self.backup = proj.backup()
        self.project = proj

    def createmodel(self, model_name, model_json, model_folder, model_group):
        """Creates a model based on a type name and a json containing properties"""

        model_path = "%s/%s.swift" % (model_folder, model_name)

        print "Preparing to edit project ..."
        print "Backup file = %s" % (self.backup)
        file_path = '%s/%s.swift' % (model_folder, model_name)

        group_arr = model_group.split("/")


        pbx_obj = None
        for group_path in group_arr:
            if pbx_obj == None:
                pbx_obj = self.project.get_or_create_group(group_path)
            else:
                previous = pbx_obj
                pbx_obj = self.project.get_or_create_group(group_path, parent=previous)

        self.project.add_file(file_path, parent=pbx_obj, force=False)
        self.project.save()

        swift_str = Model(model_name, model_json).swift_implementation
        print "--- Writing Swift code ..."
        print swift_str
        print "---"

        model_file = open(model_path, "w")
        model_file.write(swift_str)
        model_file.close()

def create_models(valid_args):
    """Start writing models into xcode project"""

    # Init Variables
    models_json = json.loads(valid_args[0])
    project_name = valid_args[1]
    model_folder = valid_args[2]
    model_group = valid_args[3]

    creator = ModelCreator(project_name)

    for key in models_json.keys():
        model_json = models_json[key]
        creator.createmodel(key, model_json, model_folder, model_group)

    print "--- Writing to files finished with success! ---"
    print "--- Cleaning up ... ---"
    try:
        os.remove(creator.backup)
    except OSError:
        pass
    print "--- Done ---"
