from PySide2 import QtGui, QtCore, QtWidgets
from .LabelsLoader import LabelsLoader
from .graphview import GraphView
from .FileExplorer import FileExplorer
from .Outline import Outline
from .Breadcrumb import Breadcrumb
from .FileTabs import FileTabs

from views import NodeGraph

class Editor:
    def __init__(self, rootPath="."):
        self.loader = LabelsLoader()

        self.horizontalSplitter = QtWidgets.QSplitter()
        self.horizontalSplitter.setWindowTitle("Nodal editor")

        self.leftPanel = QtWidgets.QSplitter(QtCore.Qt.Vertical, self.horizontalSplitter)

        self.fileExplorer = FileExplorer(editor=self, parent=self.leftPanel, path=rootPath)
        self.outline = Outline(editor=self, parent=self.leftPanel)

        self.fileTabs = FileTabs(editor=self, parent=self.horizontalSplitter)
        self.breadcrumb = Breadcrumb(editor=self, parent=None)
        self.cacheFile(rootPath)
    
    def cacheFile(self, filepath):
        self.loader.loadFromFilepath(filepath)

    def openFile(self, filepath):
        labels = self.loader.loadFromFilepath(filepath)
        self.fileExplorer.updateFilepath(filepath)
        self.fileTabs.openLabels(labels, filepath)
        self.updateGraphScene()
    
    def updateGraphScene(self):
        graphView = self.fileTabs.getCurrentGraphScene()
        if graphView:
            nodeGraph = graphView.nodeGraph
        else:
            nodeGraph = NodeGraph()

        self.outline.setNodeGraph(nodeGraph)
        self.breadcrumb.setNodeGraph(nodeGraph)

    def findLabel(self, label, search=True):
        graphView = self.fileTabs.getCurrentGraphScene()
        if graphView is None:
            return

        view = graphView.getView("label {0}".format(label))
        if view is not None:
            self.findNode(view)
            return

        if not search:
            return

        filepath = self.loader.getLabelFilepath(label)
        if filepath is not None:
            self.openFile(filepath)
            self.findLabel(label, search=False)
    
    def findNode(self, node):
        graphView = self.fileTabs.getCurrentGraphScene() 
        if graphView:
            graphView.focusItem(node)
        self.outline.focusView(node)
        self.breadcrumb.focusView(node)
    
    def show(self):
        self.horizontalSplitter.show()