from PySide2 import QtGui, QtCore, QtWidgets
from editor import Editor

import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")

    args = parser.parse_args()
    if not os.path.isdir(args.dir):
        print("Expected a directory for editor")
        return 1
    

    app = QtWidgets.QApplication([]) 
    editor = Editor(args.dir)
    editor.show()

    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())