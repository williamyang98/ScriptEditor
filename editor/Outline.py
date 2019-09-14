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
        self.tree_view.setRootIndex(QtCore.QModelIndex())
        self.tree_view.expandAll() # tree view cannot see all nodes until expanded
        self.tree_view.collapseAll()
        self.tree_view.update()
    
    def _onClick(self, index):
        node = self.model.getNodeFromIndex(index)
        view = node.view
        self.editor.findNode(view)
    
    def focusView(self, view):
        modelNode = self.model.getNodeFromView(view)
        index = self.model.getIndexFromNode(modelNode)
        if index:
            self.tree_view.setExpanded(index, True)
            self.tree_view.setCurrentIndex(index)