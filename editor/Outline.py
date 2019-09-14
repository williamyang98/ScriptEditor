from PySide2 import QtGui, QtCore, QtWidgets
from .node_graph_model import NodeGraphModel

class Outline:
    def __init__(self, editor, parent):
        self.editor = editor

        self.model = NodeGraphModel([])

        self.tree_view = QtWidgets.QTreeView(parent=parent)
        self.tree_view.setModel(self.model)

        self.tree_view.clicked.connect(self._onClick)
    
    def setNodeGraph(self, nodeGraph):
        self.model = NodeGraphModel(nodeGraph.labels)
        self.tree_view.setModel(self.model)
        self.tree_view.update()
    
    def _onClick(self, index):
        node = self.model.getNode(index)
        view = node.view
        self.editor.findNode(view)
    
    def updateView(self, view):
        pass