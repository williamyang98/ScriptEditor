from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node
from .Socket import Socket

class ContextView(Node):
    def __init__(self, context):
        super().__init__()
        self._context = context
        self._createSockets()
    
    def _createSockets(self):
        socket = Socket(self)
        self.addSocket("root", socket)

        for content in self._context.contents:
            if isinstance(content, str):
                continue
            socket = Socket(self)
            self.addSocket(content, socket)
    
    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignHCenter,
            "Context")