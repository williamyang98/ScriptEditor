from .Parser import Parser
from models import PythonScript, Text

class PythonScriptParser(Parser):
    def __init__(self, parent, metadata):
        self.parent = parent
        self.script = PythonScript(metadata)
        self.indent = None

    def parse_metadata(self, metadata, stack):
        if self.indent is None:
            self.indent = metadata.indent
        
        if metadata.indent < self.indent:
            self.close(metadata, stack)
            return
        
        self.script.add_line(Text(metadata.line, metadata))

    def close(self, metadata, stack):
        stack.pop()
        stack.parse_metadata(metadata)
    
    def on_child_pop(self, child):
        pass
        
    @property
    def model(self):
        return self.script
        