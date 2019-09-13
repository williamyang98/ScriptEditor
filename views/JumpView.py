from PySide2 import QtGui, QtCore, QtWidgets
from .Tag import Tag

class JumpView(Tag):
    def __init__(self, jump, browser):
        super().__init__(left=True, browser=browser)
        self._jump = jump
        self.calculateRect()

    @property
    def tag(self):
        return self._jump.label

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)

    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.browser.findLabel(self._jump.label)
        return super().mouseDoubleClickEvent(event)