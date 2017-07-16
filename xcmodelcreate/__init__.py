import sys, os
import json
from pbxproj import XcodeProject as xc
from pprint import pprint

class Token:
    def __init__(self, key, value):
        self.propertyName = key
        self.type = value
        self.conversionType = type
        self.isDate = None
        if self.type.startswith("Date"):
            self.type = "Date"
            self.isDate = True
            self.conversionType = "TimeInterval"


def runwithargs(args):

    # Init Variables
    modelsJSON = json.loads(args[0])
    projectName = args[1]
    modelFolder = args[2]

    project = xc.load('%s.xcodeproj/project.pbxproj' % (projectName))
    backup = project.backup()

    def createmodel( modelName, modelJSON ):
        modelPath = "%s/%s.swift" % (modelFolder, modelName)

        print("Preparing to edit project ...\nBackup file = %s" % (backup))
        project.add_file('%s/%s.swift' % (modelFolder, modelName), force=False)
        project.save()

        propertyKeys = modelJSON.keys()

        swiftStr = """
import Foundation

struct %s: DictionaryRepresentable {
""" % (modelName)

        codingKeys = "\tenum CodingKeys: String {\n"
        initializer = "\tpublic init("
        asDictionary = "\tpublic func asDictionary() -> [String: Any] {\n\t\treturn [\n"
        dicInitializer = "\tpublic init?(dic: [String: Any]) {\n"

        for idx, key in enumerate(propertyKeys * 2):
            token = Token(key, modelJSON[key])

            if idx < len(propertyKeys):
                codingKeys += "\t\tcase %s\n" % (key)

                initializer += "%s: %s" % (key, token.type)
                if len(initializer) > len("public init("):
                    initializer += ", "
                swiftStr += "\tpublic let %s: %s\n" % (key, token.type)
                dicInitializer += "\t\tguard let param%d = dic[CodingKeys.%s.rawValue] as? %s else { return nil }\n" % (idx, key, token.conversionType)

                if token.isDate:
                    dicInitializer += "\t\tself.%s = Date(timeIntervalSince1970: param%d)\n" % (key, idx)
                    asDictionary += "\t\t\tCodingKeys.%s.rawValue: self.%s.timeIntervalSince1970,\n" % (key, key)
                else:
                    dicInitializer += "\t\tself.%s = param%d\n" % (key, idx)
                    asDictionary += "\t\t\tCodingKeys.%s.rawValue: self.%s,\n" % (key, key)
                dicInitializer += "\n"
            else:
                if idx == len(propertyKeys):
                    # delete the last ','
                    initializer = initializer[:-2]

                    # close the initializer's parameters
                    initializer += ") {\n"

                initializer += "\t\tself.%s = %s\n" % (key, key)

        codingKeys += "\t}"
        initializer += "\t}"
        dicInitializer = dicInitializer[:-1]
        dicInitializer += "\t}"
        asDictionary = asDictionary[:-2]
        asDictionary += "\n\t\t]\n\t}"
        swiftStr += "\n%s\n\n%s\n\n%s\n\n%s\n}" % (codingKeys, initializer, dicInitializer, asDictionary)
        print(swiftStr)

        file = open(modelPath, "w")
        file.write(swiftStr)
        file.close()

    for key in modelsJSON.keys():
        modelJSON = modelsJSON[key]
        createmodel(key, modelJSON)

    print("--- Writing to files finished with success! ---")
    print("--- Cleaning up ... ---")
    try:
        os.remove(backup)
    except OSError:
        pass
    print("--- Done ---")
