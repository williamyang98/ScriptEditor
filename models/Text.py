from .Node import Node

class Text(Node):
    def __init__(self, text, metadata):
        super().__init__(metadata)
        self.text = text

    def accept(self, visitor):
        return visitor.visit_text(self)