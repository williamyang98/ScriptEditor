from PySide2 import QtCore
from .Organiser import Organiser
from .ViewGroup import ViewGroup

class TreeOrganiser(Organiser):
    def __init__(self):
        self.x_padding = 50
        self.y_padding = 50
    
    def organise(self, nodeGraph):
        viewGroups = [ViewGroup(label) for label in nodeGraph.labels]
        for viewGroup in viewGroups:
            self._organiseViewGroup(viewGroup)
        height = sum((vg.boundingRect.height() for vg in viewGroups))
        height += self.y_padding * (len(viewGroups)-1)

        y_centre = height/2

        y = -y_centre 
        x = 0
        for viewGroup in viewGroups:
            viewGroup.position = QtCore.QPointF(x-viewGroup.boundingRect.width()/2, y)
            y += viewGroup.boundingRect.height() + self.y_padding

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
        width = max((c.boundingRect.width() for c in group.children), default=0)

        y = group.rootRect.center().y() - height/2
        x = group.rootRect.right() + max([self.y_padding, height/10, group.rootRect.height()/10]) 
        for child in group.children:
            child.position = QtCore.QPointF(x, y)
            y += self.y_padding + child.boundingRect.height()
        # recalculate bounding box
        group.updateBoundingRect()