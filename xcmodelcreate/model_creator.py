# -*- coding: utf-8 -*-
"""model_creator.py"""
import os
import json
from xcmodelcreate import Model
from xcmodelcreate import Config
from pbxproj import XcodeProject as xc

def createmodel(model_name, model_json, model_folder, model_group, project):
    """Creates a model based on a type name and a json containing properties"""

    model_path = "%s/%s.swift" % (model_folder, model_name)

    file_path = '%s/%s.swift' % (model_folder, model_name)

    group_arr = model_group.split("/")

    pbx_obj = None
    for group_path in group_arr:
        if pbx_obj is None:
            pbx_obj = project.get_or_create_group(group_path)
        else:
            previous = pbx_obj
            pbx_obj = project.get_or_create_group(group_path, parent=previous)

    project.add_file(file_path, parent=pbx_obj, force=False)
    project.save()

    swift_str = Model(model_name, model_json).swift_implementation
    print "--- Writing Swift code for \"%s\"" % (model_name)

    model_file = open(model_path, "w")
    model_file.write(swift_str)
    model_file.close()

def create_models():
    """Start writing models into xcode project"""

    models_json = None
    model_folder = None
    model_group = None

    # Init Variables
    config = Config()

    model_json_path = config.json_path
    xcodeproj_path = config.xcproject_path
    model_folder = config.model_folder
    model_group = config.model_group

    with open(model_json_path, 'r') as json_file:
        models_json = json.load(json_file)

    proj = xc.load('%s/project.pbxproj' % (xcodeproj_path))
    backup = proj.backup()

    print "Preparing to edit project ..."
    print "Backup file = %s" % (backup)

    for key in models_json:
        model_json = models_json[key]
        createmodel(key, model_json, model_folder, model_group, proj)

    print "--- Writing to files finished with success! ---"
    print "--- Cleaning up ... ---"
    try:
        os.remove(backup)
    except OSError:
        pass
    print "--- Done ---"
