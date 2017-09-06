"""main.py"""

import sys
from xcmodelcreate import model_creator
from xcmodelcreate import validator

def main():
    """The main function of the applications"""

    print "--- www.DeveloThor.codes ---"
    print "--- validating inputs ... ---"

    args = sys.argv
    del args[0]
    if validator.validate(sys.argv):
        model_creator.create_models(sys.argv)
    else:
        sys.exit(-1)
