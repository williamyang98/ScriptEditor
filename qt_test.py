from PySide2 import QtGui, QtCore, QtWidgets

from OrganiserControls import OrganiserControls

from views import View, Renderer, Organiser, TreeOrganiser
from models import JSONSerialiser
from script_parser import parse_lines


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
    renderer = Renderer(scene, organiser)
    with open("story/Day 1/4 engineering.rpy") as fp:
        labels = parse_lines(fp.readlines())
    
    serialiser = JSONSerialiser()
    data = [label.accept(serialiser) for label in labels]

    with open("parsed.json", "w") as fp:
        json.dump(data, fp, indent=2)

    for label in labels:
        label.accept(renderer)

    controls = OrganiserControls(None, organiser)
    
    organiser.organise()

    splitter.show()
    controls.show()

    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())