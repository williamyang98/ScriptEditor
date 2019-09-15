from .Node import Node

class Label(Node):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.context = None

    @property
    def children(self):
        if self.context:
            return [self.context]
        return []
    
    def accept(self, visitor):
        return visitor.visit_label(self)
