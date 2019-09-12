from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node
from .Socket import Socket

class ContextView(Node):
    def __init__(self, context):
        super().__init__(colour=QtGui.QColor(0, 0, 255, 50))
        self._context = context
        self._createSockets()
        self.min_width = 100
        self.x_padding = 10
        self.y_padding = 5
    
    def _createSockets(self):
        socket = Socket(self)
        self.addSocket("root", socket)
        for content in self._context.contents:
            if isinstance(content, str):
                continue
            socket = Socket(self)
            self.addSocket(content, socket)
    
    def paint(self, painter, option, widget):
        fontMetrics = painter.fontMetrics()
        height = (fontMetrics.height() + self.y_padding) * (len(self._context.contents)+1)
        width = max([fontMetrics.width(c) for c in self._context.contents if isinstance(c, str)]+[self.min_width])
        width += 2*self.x_padding

        self.height = height
        self.width = width

        super().paint(painter, option, widget)

        self.alignSocketLeft(self.getSocket("root"))

        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignHCenter,
            "Context")
        
        y = fontMetrics.height()+self.y_padding
        for content in self._context.contents:
            if isinstance(content, str):
                text = content
            else:
                text = str(content).upper()
                socket = self.getSocket(content)
                self.alignSocketRight(socket)
                socket_y = y+fontMetrics.height()/2-socket.boundingRect().height()/2
                socket.setPos(QtCore.QPoint(socket.pos().x(), socket_y))

            painter.drawText(
                QtCore.QRectF(self.x_padding, y, width, fontMetrics.height()),
                QtCore.Qt.AlignLeft,
                text)
            
            y += fontMetrics.height()+self.y_padding
            
