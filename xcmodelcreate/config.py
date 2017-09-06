import json

class Config(object):
    json_path = None
    model_folder = None
    model_group = None

    def __init__(self):
        config_path = "./.xcmodelcreate/config.json"
        with open(config_path) as data_file:
            json_all = json.load(data_file)
            self.json_path = json_all["json_path"]
            self.model_folder = json_all["model_folder"]
            self.model_group = json_all["model_group"]
