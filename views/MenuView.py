from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node
from .Socket import Socket

class MenuView(Node):
    def __init__(self, menu):
        super().__init__()
        self._menu = menu
        self._createSockets()
        self.min_width = 100
        self.x_padding = 10
        self.y_padding = 5
    
    def _createSockets(self):
        socket = Socket(self)
        self.addSocket("root", socket)
        for choice in self._menu.choices:
            socket = Socket(self)
            self.addSocket(choice, socket)
    
    def paint(self, painter, option, widget):
        fontMetrics = painter.fontMetrics()
        height = (fontMetrics.height() + self.y_padding) * (len(self._menu.choices)+2)
        width = max(
            [fontMetrics.width("Choice: {0}".format(c.description)) for c in self._menu.choices] +
            [self.min_width] +
            [fontMetrics.width("Description: {0}".format(self._menu.description))])
        width += 2*self.x_padding

        self.height = height
        self.width = width

        super().paint(painter, option, widget)

        self.alignSocketLeft(self.getSocket("root"))

        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignHCenter,
            "Menu")
        
        y = fontMetrics.height()+self.y_padding

        painter.drawText(
            QtCore.QRectF(self.x_padding, y, width, fontMetrics.height()),
            QtCore.Qt.AlignLeft,
            "Description: {0}".format(self._menu.description))

        y += fontMetrics.height()+self.y_padding

        for choice in self._menu.choices:
            text = "Choice: {0}".format(choice.description) 
            socket = self.getSocket(choice)
            self.alignSocketRight(socket)
            socket_y = y+fontMetrics.height()/2-socket.boundingRect().height()/2
            socket.setPos(QtCore.QPoint(socket.pos().x(), socket_y))

            painter.drawText(
                QtCore.QRectF(self.x_padding, y, width, fontMetrics.height()),
                QtCore.Qt.AlignLeft,
                text)
            
            y += fontMetrics.height()+self.y_padding