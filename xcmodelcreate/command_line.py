import xcmodelcreate
import sys

def validate(args):
    argNames = [ "modelsJSON", "projectName", "modelFolder" ]
    valid = True
    print(args)
    if len(args) < 3:
        valid = None
        i = len(args)
        while i < 3:
            print("Missing input for %s" % (argNames[i]))
            i += 1
    elif len(args) > 4:
        valid = None
        print("Too many arguments! Arguments are:")
        for idx, e in enumerate(argNames):
            print("args[%d] = %s" % (idx, e))
    return valid

def main():

    print("""
--- www.DeveloThor.codes ---

--- validating inputs ... ---
""")

    args = sys.argv
    del args[0]
    if validate(sys.argv):
        print(xcmodelcreate.runwithargs(sys.argv))
    else:
        sys.exit(-1)
