from .Node import Node

class Label(Node):
    def __init__(self, name, metadata):
        super().__init__(metadata)
        self.name = name
        self.context = None

    @property
    def children(self):
        if self.context:
            return [self.context]
        return []
    
    def accept(self, visitor):
        return visitor.visit_label(self)
