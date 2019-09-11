from .Visitable import Visitable

class Label(Visitable):
    def __init__(self, name):
        self.name = name
        self.context = None
    
    def accept(self, visitor):
        return visitor.visit_label(self)
