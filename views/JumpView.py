from PySide2 import QtGui, QtCore, QtWidgets
from .Tag import Tag

class JumpView(Tag):
    def __init__(self, jump):
        super().__init__(left=True)
        self._jump = jump
        self.calculateRect()

    @property
    def tag(self):
        return self._jump.label

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)