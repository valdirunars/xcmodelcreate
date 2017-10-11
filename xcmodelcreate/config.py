# -*- coding: utf-8 -*-
import sys
import json

class Config(object):
    json_path = None
    model_folder = None
    xcproject_path = None
    model_group = None

    def __init__(self):
        config_path = "./.xcmodelcreate/config.json"
        try:
            with open(config_path) as data_file:
                json_all = json.load(data_file)
                self.json_path = json_all["json_path"]
                self.xcproject_path = json_all["xcproj"]
                self.model_folder = json_all["model_folder"]
                self.model_group = json_all["model_group"]
        except IOError:
            print "--- Error: xcmodelcreate not setup correctly make sure you call \"xcmodelcreate init\" and edit the generated \"./.xcmodelcreate/models.json\" ---"
            sys.exit(-1)
