from PySide2 import QtCore
from editor.organisers import Organiser

from .Base import Base
from .BasicNode import BasicNode

class TreeOrganiser(Organiser):
    def __init__(self):
        self.clear()
        self.x_padding = 50
        self.y_padding = 50
    
    def clear(self):
        self.root = Base(QtCore.QPointF(0, 0))
        self.parent = self.root
        self.last_node = self.root
    
    def __enter__(self):
        self.parent = self.last_node
    
    def __exit__(self, type, value, traceback):
        self.last_node = self.parent
        self.parent = self.last_node.parent

    def add_node(self, root):
        node = BasicNode(root, self.parent)
        self.last_node = node
        self.parent.addChild(node)
    
    def organise(self):
        self._organise_node(self.root)

    # depth first search
    def _organise_node(self, node):
        # if no children, return
        if len(node.children) == 0:
            node.updateBoundingRect()
            return
        # organise children
        for child in node.children:
            self._organise_node(child)
        # one children are ready, organise this node
        # organise in order of children
        height = sum((c.boundingRect.height() for c in node.children))
        height += (self.y_padding * (len(node.children)-1))
        width = max((c.boundingRect.width() for c in node.children))

        y = node.rootRect.center().y() - height/2
        x = node.rootRect.right() + self.x_padding
        for child in node.children:
            child.position = QtCore.QPointF(x, y)
            y += self.y_padding + child.boundingRect.height()
        # recalculate bounding box
        node.updateBoundingRect()