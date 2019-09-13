from PySide2 import QtCore

class Browser:
    def __init__(self, view):
        self.labels = {}
        self.view = view

    def clear(self):
        self.view.scene().clear()
        self.centreOn(QtCore.QPointF(0, 0))
        self.labels = {}
    
    def addItem(self, item):
        self.view.scene().addItem(item)

    def addLabel(self, label, view):
        self.labels.setdefault(label, view)

    def findLabel(self, label):
        view = self.labels.get(label)
        if view is not None:
            self.centreOn(view.pos())

    def centreOn(self, position):
        self.view.centerOn(position)
