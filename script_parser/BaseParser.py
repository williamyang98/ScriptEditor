from models import Label, MetaData
import re

from .Parser import Parser
from .ContextParser import ContextParser
from .ParseException import ParseException

regex_label = re.compile(r"label\s+(?P<label>[A-Za-z0-9_\-]+)\s*:")

class BaseParser(Parser):
    """Gets all labels and their contexts from lines
    """
    def __init__(self):
        self._labels = []
        self.label = None
        self.child = None

    def parse_line(self, metadata):
        if self.child:
            self.child.parse_line(metadata)
            # if child still active
            if self.child:
                return

        # ignore if not aligned to 0
        if metadata.indent != 0:
            return
        
        match = regex_label.match(metadata.line)
        if match:
            label = match["label"]
            self.child = ContextParser(self, metadata)
            self.label = Label(label, metadata)
    
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
        

