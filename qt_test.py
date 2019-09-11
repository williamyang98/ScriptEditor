from PySide2 import QtGui, QtCore, QtWidgets
from views import Node, View
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

    tree_view = QtWidgets.QTreeView(parent=splitter)
    tree_view.setModel(model)
    tree_view.setRootIndex(model.index(args.dir))

    # scene
    scene = QtWidgets.QGraphicsScene()
    scene.addItem(Node("Node A", QtGui.QColor(255, 0, 0)))
    view = View(scene, splitter)

    splitter.setWindowTitle("Nodal editor")
    splitter.show()

    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())