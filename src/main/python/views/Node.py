from PySide2 import QtGui, QtCore, QtWidgets
from abc import ABC

class Node(QtWidgets.QGraphicsItem):
    def __init__(self, editor, colour=QtGui.QColor(255, 255, 255)):
        super().__init__()
        self._editor = editor
        self.colour = colour 
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.width = 100
        self.height = 100
        self.sockets = {}

    @property
    def editor(self):
        return self._editor

    def addSocket(self, key, socket):
        self.sockets.setdefault(key, socket)
    
    def getSocket(self, key):
        return self.sockets.get(key)
    
    def alignSocketLeft(self, socket):
        x = self.boundingRect().left()-socket.boundingRect().width()/2
        socket.setPos(QtCore.QPointF(x, socket.pos().y()))
    
    def alignSocketRight(self, socket):
        x = self.boundingRect().right()-socket.boundingRect().width()/2
        socket.setPos(QtCore.QPointF(x, socket.pos().y()))
    
    def alignSocketVCentre(self, socket):
        y = self.boundingRect().center().y()-socket.boundingRect().height()/2
        socket.setPos(QtCore.QPointF(socket.pos().x(), y))

    def boundingRect(self):
        return QtCore.QRectF(0, 0, self.width, self.height) 
    
    def paint(self, painter, option, widget):
        palette = self.scene().palette()
        brush = palette.text()

        painter.setPen(QtGui.QPen(brush, 1.0))
        painter.setBrush(QtGui.QBrush(self.colour))
        painter.drawRoundedRect(self.boundingRect(), 5, 5)
    
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
            self.editor.findNode(self)
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
            return
        return super().mouseDoubleClickEvent(event)

        