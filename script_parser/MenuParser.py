from .Parser import Parser
from .ParseException import ParseException
from models import Menu, Choice
import re

regex_description = re.compile(r"\"(?P<description>.+)\"")
regex_choice = re.compile(r"(?P<choice>.+):")

class MenuParser(Parser):
    def __init__(self, parent, metadata):
        self.parent = parent
        self._model = Menu(metadata)
        self.indent = None

        self.child = None
        self.choice = None

    def parse_line(self, metadata):
        if self.indent is None:
            self.indent = metadata.indent

        if self.child:
            self.child.parse_line(metadata)
            if self.child:
                return
        
        if metadata.indent < self.indent:
            self.close()
            return

        self.parse_choice(metadata) or \
        self.parse_description(metadata)
        
            
    def parse_description(self, metadata):
        match = regex_description.match(metadata.line)
        if match:
            description = match["description"]
            self._model.description = description
            return True
        return False

    def parse_choice(self, metadata):
        from .ContextParser import ContextParser
        match = regex_choice.match(metadata.line)
        if match:
            description = match["choice"]
            choice = Choice(description, metadata)
            self.choice = choice
            self._model.add_choice(choice)
            self.child = ContextParser(self, metadata)
            return True
        return False
    
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
            







