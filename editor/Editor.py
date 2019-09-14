from PySide2 import QtGui, QtCore, QtWidgets
from .LabelsLoader import LabelsLoader
from .graphview import GraphView
from .FileExplorer import FileExplorer
from .Outline import Outline

class Editor:
    def __init__(self, rootPath="."):
        self.loader = LabelsLoader()

        self.horizontalSplitter = QtWidgets.QSplitter()
        self.horizontalSplitter.setWindowTitle("Nodal editor")

        self.verticalSplitter = QtWidgets.QSplitter(QtCore.Qt.Vertical, self.horizontalSplitter)

        self.fileExplorer = FileExplorer(editor=self, parent=self.verticalSplitter, path=rootPath)
        self.outline = Outline(editor=self, parent=self.verticalSplitter)

        self.graphView = GraphView(editor=self, parent=self.horizontalSplitter)

        self.cacheFile(rootPath)

    def cacheFile(self, filepath):
        self.loader.loadFromFilepath(filepath)

    def openFile(self, filepath):
        labels = self.loader.loadFromFilepath(filepath)
        self.fileExplorer.updateFilepath(filepath)
        self.graphView.open(labels)
        self.outline.setNodeGraph(self.graphView.nodeGraph)

    def findLabel(self, label, search=True):
        view = self.graphView.getView("label {0}".format(label))
        if view is not None:
            self.graphView.focusItem(view)
            return

        if not search:
            return

        filepath = self.loader.getLabelFilepath(label)
        if filepath is not None:
            self.openFile(filepath)
            self.findLabel(label, search=False)
    
    def findNode(self, node):
        self.graphView.focusItem(node)
    
    def show(self):
        self.horizontalSplitter.show()