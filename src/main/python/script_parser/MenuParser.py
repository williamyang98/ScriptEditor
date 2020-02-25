from .Parser import Parser
from .ParseException import ParseException
from models import Menu, Choice
import re

regex_description = re.compile(r"\"(?P<description>.+)\"")
regex_choice = re.compile(r"(?P<choice>.+):")

class MenuParser(Parser):
    def __init__(self, parent, metadata):
        self.parent = parent
        self.menu = Menu(metadata)
        self.indent = None

        self.choice = None

    def parse_metadata(self, metadata, stack):
        if self.indent is None:
            self.indent = metadata.indent

        if metadata.indent < self.indent:
            self.close(metadata, stack)
            return

        self.parse_choice(metadata, stack) or \
        self.parse_description(metadata, stack)
        
            
    def parse_description(self, metadata, stack):
        match = regex_description.match(metadata.line)
        if match:
            description = match["description"]
            self.menu.description = description
            return True
        return False

    def parse_choice(self, metadata, stack):
        from .ContextParser import ContextParser
        match = regex_choice.match(metadata.line)
        if match:
            description = match["choice"]
            choice = Choice(description, metadata)
            self.choice = choice
            self.menu.add_choice(choice)
            parser = ContextParser(self, metadata)
            stack.push(parser)
            return True
        return False
    
    def close(self, metadata, stack):
        stack.pop()
        stack.parse_metadata(metadata)
    
    def on_child_pop(self, child):
        self.choice.context = child.model
        self.choice = None

    @property
    def model(self):
        return self.menu
            







