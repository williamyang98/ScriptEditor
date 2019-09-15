from .BaseParser import BaseParser

class ParserStack:
    def __init__(self):
        self.stack = []
        self.base = BaseParser(self)

    def parse_metadata(self, metadata):
        top = self.get_top()
        top.parse_metadata(metadata=metadata, stack=self)

    def push(self, parser):
        self.stack.append(parser)
    
    def pop(self):
        child = self.stack.pop()
        parent = self.get_top()
        parent.on_child_pop(child)
    
    def collapse(self):
        while len(self.stack) > 0:
            self.pop()
    
    @property
    def labels(self):
        return self.base.labels
    
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return self.base
