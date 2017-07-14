import sys, os
import json
from pbxproj import XcodeProject as xc
from pprint import pprint
args = sys.argv

logo = """
--- www.DeveloThor.codes ---

validating inputs ...
"""
print(logo)
# remove first argument which is playground.py because we
# are running this by the command python playground.py

print(args)

# 1. Input Validation

argNames = [ "modelsJSON", "projectName", "modelFolder" ]
if len(args) < 3:
    i = len(args)
    while i < 4:
        print("Missing input for %s" % (argNames[i]))
        i += 1
elif len(args) > 4:
    print("Too many arguments! Arguments are:")
    for idx, e in enumerate(argNames):
        print("args[%d] = %s" % (idx, e))

print("--- Success ---")
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

    # 4. Generate Swift code

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
        type = modelJSON[key]
        conversionType = type
        dateMultiplier = ""
        if type.startswith("Date"):
            type = "Date"
            conversionType = "TimeInterval"

        if idx < len(propertyKeys):
            codingKeys += "\t\tcase %s\n" % (key)

            initializer += "%s: %s" % (key, type)
            if len(initializer) > len("public init("):
                initializer += ", "
            swiftStr += "\tpublic let %s: %s\n" % (key, type)
            dicInitializer += "\t\tguard let param%d = dic[CodingKeys.%s.rawValue] as? %s else { return nil }\n" % (idx, key, conversionType)

            if conversionType != type:
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

# The Script

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
