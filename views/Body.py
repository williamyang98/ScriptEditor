from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node

from abc import abstractproperty

class Body(Node):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.min_width = 100
        self.x_padding = 10
        self.y_padding = 5
    
    @abstractproperty
    def entries(self):
        pass
    
    def paint(self, painter, option, widget):
        fontMetrics = painter.fontMetrics()
        entries = list(self.entries)

        height = (fontMetrics.height() + self.y_padding) * (len(entries)+1)
        width = max([fontMetrics.width(s) for s,_ in entries]+[self.min_width])
        width += 2*self.x_padding

        self.height = height
        self.width = width

        super().paint(painter, option, widget)

        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignHCenter,
            self.title)
        
        y = fontMetrics.height()+self.y_padding
        for text, key in entries:
            painter.drawText(
                QtCore.QRectF(self.x_padding, y, width, fontMetrics.height()),
                QtCore.Qt.AlignLeft,
                text)
            socket = self.getSocket(key)
            if socket:
                self.alignSocketRight(socket)
                socket_y = y+fontMetrics.height()/2-socket.boundingRect().height()/2
                socket.setPos(QtCore.QPoint(socket.pos().x(), socket_y))
            y += fontMetrics.height()+self.y_padding