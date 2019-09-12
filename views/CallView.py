from PySide2 import QtGui, QtCore, QtWidgets
from .Tag import Tag

class CallView(Tag):
    def __init__(self, call):
        super().__init__(left=True)
        self._call = call

    @property
    def tag(self):
        return self._call.label

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)