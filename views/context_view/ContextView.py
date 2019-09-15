from PySide2 import QtGui, QtCore, QtWidgets
from views import Body
from views import Socket

from .ContextDescriptions import ContextDescription

descriptor = ContextDescription()

class ContextView(Body):
    def __init__(self, context, editor):
        super().__init__(title="Context", editor=editor, colour=QtGui.QColor(0, 0, 255, 50))
        self._context = context
        self._createSockets()
        self._createEntries()
        self.calculateRect()
    
    def _createSockets(self):
        socket = Socket(self)
        self.addSocket("root", socket)
    
    def _createEntries(self):
        self._entries = []
        for content in self._context.contents:
            data = content.accept(descriptor)
            if data is None:
                continue

            if data.text:
                self._entries.append((data.text, content))

            if data.hasSocket: 
                socket = Socket(self)
                self.addSocket(content, socket)
    
    @property
    def entries(self):
        return self._entries
    
    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        self.alignSocketLeft(self.getSocket("root"))