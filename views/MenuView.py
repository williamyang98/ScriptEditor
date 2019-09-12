from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node
from .Socket import Socket

class MenuView(Node):
    def __init__(self, menu):
        super().__init__()
        self._menu = menu
        self._createSockets()
    
    def _createSockets(self):
        self.addSocket("root", Socket(self))
        for choice in self._menu.choices:
            self.addSocket(choice, Socket(self))
    
    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignHCenter,
            "Menu")