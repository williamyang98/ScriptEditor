from PySide2 import QtCore
from .Node import Node

class Base(Node):
    def __init__(self, position):
        super().__init__()
        self._position = position
        self.updateBoundingRect()
    
    @property
    def parent(self):
        return self
    
    @property
    def boundingRect(self):
        return self._boundingRect
    
    @property
    def rootRect(self):
        return QtCore.QRectF(self.position.x(), self.position.y(), 0, 0)
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, pos):
        delta = pos - self.position
        self.translate(delta)

    def translate(self, delta):
        self._position += delta
        self._boundingRect.translate(delta)
        for child in self.children:
            child.translate(delta)

    def updateBoundingRect(self):
        rect = self.rootRect
        if len(self.children) == 0:
            self._boundingRect = rect
            return
        for child in self.children:
            rect = rect.united(child.boundingRect)
        self._boundingRect = rect