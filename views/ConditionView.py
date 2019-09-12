from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node
from .Socket import Socket

class ConditionView(Node):
    def __init__(self, condition):
        super().__init__()
        self._condition = condition
        self._createSockets()
        self.min_width = 100
        self.x_padding = 10
        self.y_padding = 5
    
    def _createSockets(self):
        socket = Socket(self)
        self.addSocket("root", socket)
        self.addSocket(self._condition.if_condition, Socket(self))
        for elif_condition in self._condition.elif_conditions:
            self.addSocket(elif_condition, Socket(self))
        if self._condition.else_condition:
            self.addSocket(self._condition.else_condition, Socket(self))
    
    def paint(self, painter, option, widget):
        fontMetrics = painter.fontMetrics()

        items = []
        items.append((
            "IF {0}".format(self._condition.if_condition.script),
            self._condition.if_condition))

        for elif_condition in self._condition.elif_conditions:
            items.append((
                "ELIF {0}".format(elif_condition.script),
                elif_condition))
        
        if self._condition.else_condition:
            items.append((
                "ELSE",
                self._condition.else_condition))

        height = (fontMetrics.height() + self.y_padding) * (len(items)+1)
        width = max([fontMetrics.width(s) for s,_ in items]+[self.min_width])
        width += 2*self.x_padding

        self.height = height
        self.width = width

        super().paint(painter, option, widget)


        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignHCenter,
            "Condition Block")
        
        y = fontMetrics.height()+self.y_padding
        for text, condition in items:
            painter.drawText(
                QtCore.QRectF(self.x_padding, y, width, fontMetrics.height()),
                QtCore.Qt.AlignLeft,
                text)
            socket = self.getSocket(condition)
            if socket:
                self.alignSocketRight(socket)
                socket_y = y+fontMetrics.height()/2-socket.boundingRect().height()/2
                socket.setPos(QtCore.QPoint(socket.pos().x(), socket_y))
            y += fontMetrics.height()+self.y_padding

