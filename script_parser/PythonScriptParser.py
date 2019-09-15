from .Parser import Parser
from models import PythonScript, Text

class PythonScriptParser(Parser):
    def __init__(self, parent, metadata):
        self.parent = parent
        self._model = PythonScript(metadata)
        self.indent = None

    def parse_line(self, metadata):
        if self.indent is None:
            self.indent = metadata.indent
        
        if metadata.indent < self.indent:
            self.close()
            return
        
        self._model.add_line(Text(metadata.line, metadata))

    def close(self):
        self.parent.on_child_close()
    
    def on_child_close(self):
        pass
        
    @property
    def model(self):
        return self._model
        