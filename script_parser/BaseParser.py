from .Parser import Parser
from .ContextParser import ContextParser
from .ParseException import ParseException
from models import Label
import re

regex_label = re.compile(r"label\s+(?P<label>[A-Za-z0-9_\-]+)\s*:")

class BaseParser(Parser):
    """Gets all labels and their contexts from lines
    """
    def __init__(self):
        self._labels = []
        self.label = None
        self.child = None

    def parse_line(self, indent, line_number, line, filepath):
        if self.child:
            self.child.parse_line(indent, line_number, line, filepath)
            # if child still active
            if self.child:
                return

        # ignore if not aligned to 0
        if indent != 0:
            return
        
        match = regex_label.match(line)
        if match:
            label = match["label"]
            self.child = ContextParser(self, filepath=filepath, line_number=line_number)
            self.label = Label(label, filepath=filepath, line_number=line_number)
    
    def close(self):
        if self.child:
            self.child.close()
    
    def on_child_close(self):
        self._labels.append(self.label)
        context = self.child.model
        self.label.context = context
        context.parent = self.label
        self.child = None
        self.label = None
    
    @property
    def model(self):
        return self._labels
        

