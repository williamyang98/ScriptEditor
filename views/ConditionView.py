from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node
from .Socket import Socket

class ConditionView(Node):
    def __init__(self, condition):
        super().__init__()
        self._condition = condition
        self._createSockets()
    
    def _createSockets(self):
        socket = Socket(self)
        self.alignSocketLeft(socket)
        self.addSocket("root", socket)

        self._addConditionSocket(self._condition.if_condition, Socket(self))
        for elif_condition in self._condition.elif_conditions:
            self._addConditionSocket(elif_condition, Socket(self))
        if self._condition.else_condition:
            self._addConditionSocket(self._condition.else_condition, Socket(self))
    
    def _addConditionSocket(self, key, socket):
        self.alignSocketRight(socket)
        self.addSocket(key, socket)
    
    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignHCenter,
            "Condition Block")