from PySide2 import QtCore
from .Node import Node

class BasicNode(Node):
    def __init__(self, root, parent):
        super().__init__()
        self.root = root
        self._parent = parent
        self.updateBoundingRect()
    
    @property
    def parent(self):
        return self._parent

    @property
    def rootRect(self):
        rect = QtCore.QRectF(
            self.root.boundingRect().x(),
            self.root.boundingRect().y(),
            self.root.boundingRect().width(),
            self.root.boundingRect().height())
        rect.moveTo(self.root.pos())
        return rect

    @property
    def boundingRect(self):
        return self._boundingRect
    
    @property
    def position(self):
        return self.boundingRect.topLeft()
    
    @position.setter
    def position(self, pos):
        delta = pos - self.position
        self.translate(delta)

    def translate(self, delta):
        self._boundingRect.translate(delta)
        self.root.setPos(self.root.pos()+delta)
        for child in self.children:
            child.translate(delta)
    
    def updateBoundingRect(self):
        # get initial rect
        rect = self.rootRect
        if len(self.children) == 0:
            self._boundingRect = rect
            return
        # expand rect
        for child in self.children:
            rect = rect.united(child.boundingRect)

        self._boundingRect = rect 