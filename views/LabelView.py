from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node
from .Socket import Socket

class LabelView(Node):
    def __init__(self, label):
        super().__init__()
        self._label = label
        socket = Socket(self)
        self.addSocket("root", socket)
    
    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignHCenter,
            self._label.name)
