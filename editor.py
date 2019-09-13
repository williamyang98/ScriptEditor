from PySide2 import QtGui, QtCore, QtWidgets

from editor import Manager, View
from editor.organisers import TreeOrganiser 


import json
import sys
import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")

    args = parser.parse_args()
    if not os.path.isdir(args.dir):
        print("Expected a directory for editor")
        return 1
    

    app = QtWidgets.QApplication([]) 
    splitter = QtWidgets.QSplitter()

    # files
    model = QtWidgets.QFileSystemModel()
    model.setRootPath(args.dir)
    model.setNameFilters(["*.rpy"])

    tree_view = QtWidgets.QTreeView(parent=splitter)
    tree_view.setModel(model)
    tree_view.setRootIndex(model.index(args.dir))

    # scene
    scene = QtWidgets.QGraphicsScene()
    view = View(scene, splitter)

    splitter.setWindowTitle("Nodal editor")

    # organiser = Organiser()
    organiser = TreeOrganiser()
    manager = Manager(organiser, view)
    manager.cacheFile(args.dir)

    splitter.show()

    def dummy(_):
        index = tree_view.currentIndex()
        filepath = model.filePath(index)
        manager.openFile(filepath)

    tree_view.clicked.connect(dummy)
    # controls.show()

    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())