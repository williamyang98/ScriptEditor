from abc import abstractproperty, ABC
from .Visitable import Visitable

class Node(Visitable):
    def __init__(self, metadata, parent=None):
        self.metadata = metadata
        self.parent = parent

    @property
    def children(self):
        return []