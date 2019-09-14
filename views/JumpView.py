from PySide2 import QtGui, QtCore, QtWidgets
from .Tag import Tag

class JumpView(Tag):
    def __init__(self, jump, editor):
        super().__init__(left=True, editor=editor)
        self._jump = jump
        self.calculateRect()

    @property
    def tag(self):
        return self._jump.label

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
    
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
            if self.editor.findLabel(self._jump.label):
                self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
            return
        return super().mouseDoubleClickEvent(event)