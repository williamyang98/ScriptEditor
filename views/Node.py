from PySide2 import QtGui, QtCore, QtWidgets

class Node(QtWidgets.QGraphicsItem):
    def __init__(self, title, colour=QtGui.QColor(255, 255, 255)):
        super().__init__()
        self.title = title
        self.colour = QtGui.QColor(colour.red(), colour.green(), colour.blue(), 100)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.rect = QtCore.QRectF(0, 0, 100, 100)

    def boundingRect(self):
        return self.rect 
    
    def paint(self, painter, option, widget):
        palette = self.scene().palette()
        brush = palette.text()
        painter.setPen(QtGui.QPen(brush, 1.0))

        painter.drawText(self.boundingRect(), self.title)
        painter.drawRect(self.boundingRect())
        painter.fillRect(self.boundingRect(), self.colour)

    def mousePressEvent(self, event):
        print("pressed node")