class Menu:
    def __init__(self):
        self.description = None
        self.choices = []

    def add_choice(self, choice):
        self.choices.append(choice)

class Choice:
    def __init__(self, description):
        self.description = description
        self.context = None