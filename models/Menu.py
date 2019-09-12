from .Visitable import Visitable

class Menu(Visitable):
    def __init__(self):
        self.description = None
        self.choices = []

    def add_choice(self, choice):
        self.choices.append(choice)
    
    def accept(self, visitor):
        return visitor.visit_menu(self)

    def __str__(self):
        return "menu"

class Choice(Visitable):
    def __init__(self, description):
        self.description = description
        self.context = None
    
    def accept(self, visitor):
        return visitor.visit_choice(self)