from PySide2 import QtGui, QtCore, QtWidgets
from abc import ABC

class Node(QtWidgets.QGraphicsItem):
    def __init__(self, colour=QtGui.QColor(255, 255, 255)):
        super().__init__()
        self.colour = colour 
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.width = 100
        self.height = 100
        self.sockets = {}

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

    def boundingRect(self):
        return QtCore.QRectF(0, 0, self.width, self.height) 
    
    def paint(self, painter, option, widget):
        palette = self.scene().palette()
        brush = palette.text()

        painter.setPen(QtGui.QPen(brush, 1.0))
        painter.setBrush(QtGui.QBrush(self.colour))
        painter.drawRoundedRect(self.boundingRect(), 5, 5)

        