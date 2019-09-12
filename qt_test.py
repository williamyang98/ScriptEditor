from PySide2 import QtGui, QtCore, QtWidgets
from views import Node, View, Renderer, Organiser
from script_parser import parse_lines
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
    splitter.show()

    organiser = Organiser()
    renderer = Renderer(scene, organiser)
    with open("story/dead.rpy") as fp:
        labels = parse_lines(fp.readlines())
    for label in labels:
        label.accept(renderer)
    
    organiser.organise()

    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())