from PySide2 import QtGui, QtCore, QtWidgets
from .Body import Body
from .Socket import Socket

class ConditionView(Body):
    def __init__(self, condition):
        super().__init__(title="Condition block", colour=QtGui.QColor(0, 255, 0, 50))
        self._condition = condition
        self._createSockets()
    
    def _createSockets(self):
        socket = Socket(self)
        self.addSocket("root", socket)
        self.addSocket(self._condition.if_condition, Socket(self))
        for elif_condition in self._condition.elif_conditions:
            self.addSocket(elif_condition, Socket(self))
        if self._condition.else_condition:
            self.addSocket(self._condition.else_condition, Socket(self))

    @property
    def entries(self):
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
        return items

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        self.alignSocketLeft(self.getSocket("root"))