from PySide2 import QtCore
from .Organiser import Organiser
from .ViewGroup import ViewGroup

class TreeOrganiser(Organiser):
    def __init__(self):
        self.x_padding = 50
        self.y_padding = 50
    
    def organise(self, nodeGraph):
        viewGroup = ViewGroup(nodeGraph.root)
        self._organiseViewGroup(viewGroup)

    # depth first search
    def _organiseViewGroup(self, group):
        # if no children, return
        if len(group.children) == 0:
            group.updateBoundingRect()
            return
        # organise children
        for child in group.children:
            self._organiseViewGroup(child)
        # one children are ready, organise this node
        # organise in order of children
        height = sum((c.boundingRect.height() for c in group.children))
        height += (self.y_padding * (len(group.children)-1))
        width = max((c.boundingRect.width() for c in group.children))

        y = group.rootRect.center().y() - height/2
        x = group.rootRect.right() + self.x_padding
        for child in group.children:
            child.position = QtCore.QPointF(x, y)
            y += self.y_padding + child.boundingRect.height()
        # recalculate bounding box
        group.updateBoundingRect()