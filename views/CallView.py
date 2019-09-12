from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node
from .Socket import Socket

class CallView(Node):
    def __init__(self, call):
        super().__init__()
        self._call = call
        socket = Socket(self)
        self.addSocket("root", socket)
        self.alignSocketLeft(socket)
    
    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignHCenter,
            self._call.label)