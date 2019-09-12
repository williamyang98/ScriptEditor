from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node
from .Socket import Socket

class JumpView(Node):
    def __init__(self, jump):
        super().__init__()
        self._jump = jump
        self.addSocket("root", Socket(self))
    
    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignHCenter,
            self._jump.label)