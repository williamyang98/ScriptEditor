from .Node import Node

class Text(Node):
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text

    def accept(self, visitor):
        return visitor.visit_text(self)