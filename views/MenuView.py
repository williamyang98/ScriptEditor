from PySide2 import QtGui, QtCore, QtWidgets
from .Body import Body
from .Socket import Socket

class MenuView(Body):
    def __init__(self, menu):
        super().__init__(title="Menu", colour=QtGui.QColor(255, 0, 0, 50))
        self._menu = menu
        self._createSockets()
        self.calculateRect()
    
    def _createSockets(self):
        socket = Socket(self)
        self.addSocket("root", socket)
        for choice in self._menu.choices:
            socket = Socket(self)
            self.addSocket(choice, socket)
    
    @property
    def entries(self):
        entries = []
        entries.append(("Description: {0}".format(self._menu.description), None))
        for choice in self._menu.choices:
            text = "Choice: {0}".format(choice.description) 
            entries.append((text, choice))
        return entries
    
    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        self.alignSocketLeft(self.getSocket("root"))