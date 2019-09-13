from PySide2 import QtGui, QtCore, QtWidgets
from .Tag import Tag

class CallView(Tag):
    def __init__(self, call, browser):
        super().__init__(left=True, browser=browser)
        self._call = call
        self.calculateRect()

    @property
    def tag(self):
        return self._call.label

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
    
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
            self.browser.findLabel(self._call.label)
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
            return
        return super().mouseDoubleClickEvent(event)