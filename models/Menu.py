from .Node import Node

class Menu(Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = None
        self.choices = []
    
    @property
    def children(self):
        return self.choices

    def add_choice(self, choice):
        self.choices.append(choice)
    
    def accept(self, visitor):
        return visitor.visit_menu(self)

    def __str__(self):
        return "menu"

class Choice(Node):
    def __init__(self, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = description
        self.context = None
    
    @property
    def children(self):
        if self.context:
            return [self.context]
        return []
    
    def accept(self, visitor):
        return visitor.visit_choice(self)