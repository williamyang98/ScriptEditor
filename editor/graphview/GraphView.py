from PySide2 import QtGui, QtCore, QtWidgets
from .Camera import Camera

from views import NodeGraph, Renderer
from editor.organisers import TreeOrganiser, GridOrganiser
from editor import NodeTracker

class GraphView(Camera):
    def __init__(self, editor, parent):
        self._scene = QtWidgets.QGraphicsScene()
        super().__init__(scene=self._scene, parent=parent)
        self.editor = editor
        self.organiser = TreeOrganiser()
        self.nodeTracker = NodeTracker()
        self.trackedViews = {}

        self.nodeGraph = NodeGraph()
    
    def clear(self):
        self.nodeGraph = NodeGraph()
        self._scene.clear()
    
    def open(self, labels=[]):
        self.clear()
        renderer = Renderer(self._scene, self.editor)
        for label in labels:
            label.accept(renderer)
        self.nodeGraph = renderer.nodeGraph
        self._trackNodeGraph(self.nodeGraph)
        self.organise()
        self.focusPosition(QtCore.QPointF(0, 0))
    
    def organise(self, organiser=None):
        if organiser is None:
            organiser = self.organiser
        organiser.organise(self.nodeGraph)

    def getView(self, id):
        return self.trackedViews.get(id)

    def focusItem(self, item):
        pos = item.mapToScene(item.boundingRect().center())
        self.focusPosition(pos)

    def focusPosition(self, position):
        self.centerOn(position)

    def _trackNodeGraph(self, nodeGraph):
        for label in nodeGraph.labels:
            self._trackNode(label)

    def _trackNode(self, node):
        id = node.model.accept(self.nodeTracker)
        if id is not None:
            self.trackedViews.setdefault(id, node.view)
        for child in node.children:
            self._trackNode(child)