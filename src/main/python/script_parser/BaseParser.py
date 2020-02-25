from models import Label, MetaData
import re

from .Parser import Parser
from .ContextParser import ContextParser
from .ParseException import ParseException

regex_label = re.compile(r"label\s+(?P<label>[A-Za-z0-9_\-]+)\s*:")

class BaseParser(Parser):
    """Gets all labels and their contexts from lines
    """
    def __init__(self, stack):
        self.labels = []
        self.current_label = None
        self.stack = stack

    def parse_metadata(self, metadata, stack):
        # ignore if not aligned to 0
        if metadata.indent != 0:
            return
        
        match = regex_label.match(metadata.line)
        if match:
            label = match["label"]
            self.current_label = Label(label, metadata)
            parser = ContextParser(self, metadata)
            stack.push(parser)
            return
    
    def on_child_pop(self, child):
        self.labels.append(self.current_label)
        self.current_label.context = child.model
        self.current_label = None
    
    @property
    def model(self):
        return self.labels
        

