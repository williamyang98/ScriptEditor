from PySide2 import QtGui, QtCore, QtWidgets
from .Camera import Camera

from views import NodeGraph, Renderer
from editor.organisers import TreeOrganiser, GridOrganiser

class GraphView:
    def __init__(self, editor, parent):
        self.editor = editor
        self.scene = QtWidgets.QGraphicsScene()
        self.camera = Camera(self.scene, parent)

        self.organiser = TreeOrganiser()
        self.nodeGraph = NodeGraph()
    
    def clear(self):
        self.nodeGraph = NodeGraph()
        self.scene.clear()
    
    def open(self, labels=[]):
        self.clear()
        renderer = Renderer(self.scene, self.editor)
        for label in labels:
            label.accept(renderer)
        self.nodeGraph = renderer.nodeGraph
        self.organise()
    
    def organise(self, organiser=None):
        if organiser is None:
            organiser = self.organiser
        organiser.organise(self.nodeGraph)


    def focusItem(self, item):
        pos = item.mapToScene(item.boundingRect().center())
        self.focusPosition(pos)

    def focusPosition(self, position):
        self.camera.centerOn(position)