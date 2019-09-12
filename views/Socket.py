from PySide2 import QtGui, QtCore, QtWidgets

class Socket(QtWidgets.QGraphicsItem):
    def __init__(self, parent, radius=3.5):
        super().__init__(parent)
        self._rect = QtCore.QRectF(0, 0, 2*radius, 2*radius)
    
    def boundingRect(self):
        return self._rect
    
    def paint(self, painter, option, widget):
        painter.setBrush(QtGui.QBrush())
        painter.setPen(QtGui.QPen())

        painter.drawEllipse(self.boundingRect())

