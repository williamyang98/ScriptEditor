from PySide2 import QtGui, QtCore, QtWidgets
from .Camera import Camera
from .NodeTracker import NodeTracker

from views import NodeGraph, Renderer
from editor.organisers import TreeOrganiser, GridOrganiser

class GraphView(QtWidgets.QWidget):
    def __init__(self, editor, parent):
        super().__init__(parent=parent)
        self.editor = editor
        self.scene = QtWidgets.QGraphicsScene()
        self.camera = Camera(self.scene, self)

        self.organiser = TreeOrganiser()
        self.nodeGraph = NodeGraph()
        self.nodeTracker = NodeTracker(self.nodeGraph)
    
    def clear(self):
        self.nodeGraph = NodeGraph()
        self.nodeTracker = NodeTracker(self.nodeGraph)
        self.scene.clear()
    
    def open(self, labels=[]):
        self.clear()
        renderer = Renderer(self.scene, self.editor)
        for label in labels:
            label.accept(renderer)
        self.nodeGraph = renderer.nodeGraph
        self.nodeTracker = NodeTracker(self.nodeGraph)
        self.organise()
        self.focusPosition(QtCore.QPointF(0, 0))
    
    def organise(self, organiser=None):
        if organiser is None:
            organiser = self.organiser
        organiser.organise(self.nodeGraph)

    def getView(self, id):
        return self.nodeTracker.getView(id)

    def focusItem(self, item):
        pos = item.mapToScene(item.boundingRect().center())
        self.focusPosition(pos)

    def focusPosition(self, position):
        self.camera.centerOn(position)