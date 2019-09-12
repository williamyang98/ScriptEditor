from PySide2 import QtGui, QtCore, QtWidgets
from .Tag import Tag

class LabelView(Tag):
    def __init__(self, label):
        super().__init__(left=False)
        self._label = label

    @property
    def tag(self):
        return self._label.name

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)