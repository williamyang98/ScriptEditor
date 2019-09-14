from PySide2 import QtGui, QtCore, QtWidgets
from .node_graph_model import NodeGraphModel

# TODO: Use an abstract list model for the breadcrumb
class Breadcrumb:
    def __init__(self, editor, parent):
        self.editor = editor

        self.model = NodeGraphModel([])

        self.list_view = QtWidgets.QListView(parent=parent)
        self.list_view.setModel(self.model)

        self.list_view.clicked.connect(self._onClick)
    
    def setNodeGraph(self, nodeGraph):
        self.model = NodeGraphModel(nodeGraph.labels)
        self.list_view.setModel(self.model)
        self.list_view.update()
    
    def _onClick(self, index):
        node = self.model.getNodeFromIndex(index)
        view = node.view
        self.editor.findNode(view)
    
    def focusView(self, view):
        modelNode = self.model.getNodeFromView(view)
        index = self.model.getIndexFromNode(modelNode)
        if index:
            self.list_view.setCurrentIndex(index)