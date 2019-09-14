from PySide2 import QtCore

class ViewGroup:
    def __init__(self, node):
        self.root = node.view 
        self.children = [ViewGroup(child) for child in node.children]
        self._boundingRect = self._calculateBoundingRect()

    @property
    def rootRect(self):
        if self.root is None:
            return QtCore.QRectF(0, 0, 0, 0)

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
        if self.root is not None:
            self.root.setPos(self.root.pos()+delta)
        for child in self.children:
            child.translate(delta)

    def updateBoundingRect(self):
        self._boundingRect = self._calculateBoundingRect()

    def _calculateBoundingRect(self):
        rect = self.rootRect
        for child in self.children:
            rect = rect.united(child.boundingRect)
        return rect
