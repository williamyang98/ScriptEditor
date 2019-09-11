from PySide2 import QtGui, QtCore, QtWidgets

class Node(QtWidgets.QGraphicsItem):
    def __init__(self, title, colour=QtGui.QColor(255, 255, 255)):
        super().__init__()
        self.title = title
        self.colour = QtGui.QColor(colour.red(), colour.green(), colour.blue(), 100)

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 100, 100)
    
    def paint(self, painter, option, widget):
        palette = self.scene().palette()
        brush = palette.text()
        painter.setPen(QtGui.QPen(brush, 1.0))

        painter.drawText(self.boundingRect(), self.title)
        painter.drawRect(self.boundingRect())
        painter.fillRect(self.boundingRect(), self.colour)