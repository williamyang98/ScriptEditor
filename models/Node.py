from abc import abstractproperty, ABC
from .Visitable import Visitable

class Node(Visitable):
    def __init__(self, filepath, line_number, parent=None):
        self.filepath = filepath
        self.line_number = line_number
        self.parent = parent

    @property
    def children(self):
        return []