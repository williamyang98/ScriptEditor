from PySide2 import QtGui, QtCore, QtWidgets
from .Body import Body
from .Socket import Socket

class ContextView(Body):
    def __init__(self, context, browser):
        super().__init__(title="Context", browser=browser, colour=QtGui.QColor(0, 0, 255, 50))
        self._context = context
        self._createSockets()
        self.calculateRect()
    
    def _createSockets(self):
        socket = Socket(self)
        self.addSocket("root", socket)
        for content in self._context.contents:
            if isinstance(content, str):
                continue
            socket = Socket(self)
            self.addSocket(content, socket)
    
    @property
    def entries(self):
        entries = []
        for content in self._context.contents:
            if isinstance(content, str):
                entries.append((content, None))
            else:
                text = str(content)
                entries.append((text, content))
        return entries
    
    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        self.alignSocketLeft(self.getSocket("root"))