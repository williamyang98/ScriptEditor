from PySide2 import QtGui, QtCore, QtWidgets
from .Body import Body
from .Socket import Socket

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
        for content in self._context.contents:
            if isinstance(content, str):
                continue
            socket = Socket(self)
            self.addSocket(content, socket)
    
    def _createEntries(self):
        self._entries = []
        for content in self._context.contents:
            if isinstance(content, str):
                self._entries.append((content, None))
            else:
                text = str(content)
                self._entries.append((text, content))
    
    @property
    def entries(self):
        return self._entries
    
    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        self.alignSocketLeft(self.getSocket("root"))