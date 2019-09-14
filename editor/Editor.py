from PySide2 import QtGui, QtCore, QtWidgets
from .LabelsLoader import LabelsLoader
from .graphview import GraphView
from .FileExplorer import FileExplorer

class Editor:
    def __init__(self, rootPath="."):
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setWindowTitle("Nodal editor")

        self.fileExplorer = FileExplorer(editor=self, parent=self.splitter, path=rootPath)
        self.loader = LabelsLoader()

        self.graphView = GraphView(editor=self, parent=self.splitter)

        self.cacheFile(rootPath)

    def cacheFile(self, filepath):
        self.loader.loadFromFilepath(filepath)

    def openFile(self, filepath):
        labels = self.loader.loadFromFilepath(filepath)
        self.graphView.open(labels)

    def findLabel(self, label):
        pass

    def findNode(self, node):
        self.graphView.focusItem(node)
    
    def show(self):
        self.splitter.show()