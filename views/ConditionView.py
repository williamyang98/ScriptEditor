from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node
from .Socket import Socket

class ConditionView(Node):
    def __init__(self, condition):
        super().__init__()
        self._condition = condition
        self._createSockets()
    
    def _createSockets(self):
        self.addSocket("root", Socket(self))
        self.addSocket(self._condition.if_condition, Socket(self))
        for elif_condition in self._condition.elif_conditions:
            self.addSocket(elif_condition, Socket(self))
        if self._condition.else_condition:
            self.addSocket(self._condition.else_condition, Socket(self))
    
    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignHCenter,
            "Condition Block")