from .Parser import Parser
from models import Menu, Choice
import re

regex_description = re.compile(r"\"(?P<description>.+)\"")
regex_choice = re.compile(r"\"(?P<choice>.+)\":")

class MenuParser(Parser):
    def __init__(self, parent):
        self.parent = parent
        self._model = Menu()
        self.indent = None

        self.child = None
        self.choice = None

        self.line_parser = self.parse_description

    def parse_line(self, indent, line_number, line):
        if self.indent is None:
            self.indent = indent

        if self.child:
            self.child.parse_line(indent, line_number, line)
            if self.child:
                return
        
        if indent > self.indent:
            self.close()
            return

        self.line_parser(indent, line_number, line)
        
            
    def parse_description(self, indent, line_number, line):
        match = regex_description.match(line)
        if match:
            description = match["description"]
            self._model.description = description
            self.line_parser = self.parse_choice

    def parse_choice(self, indent, line_number, line):
        from .ContextParser import ContextParser
        match = regex_choice.match(line)
        if match:
            description = match["choice"]
            choice = Choice(description)
            self.choice = choice
            self._model.add_choice(choice)
            self.child = ContextParser(self)
    
    def close(self):
        if self.child:
            self.child.close()
        self.parent.on_child_close()
        
    
    def on_child_close(self):
        sub_model = self.child.model
        self.choice.context = sub_model
        sub_model.parent = self.choice
        self.choice = None
        self.child = None


    @property
    def model(self):
        return self._model
            







