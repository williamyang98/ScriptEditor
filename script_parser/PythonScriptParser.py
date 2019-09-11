from .Parser import Parser
from models import PythonScript

class PythonScriptParser(Parser):
    def __init__(self, parent):
        self.parent = parent
        self._model = PythonScript()
        self.indent = None

    def parse_line(self, indent, line_number, line):
        if self.indent is None:
            self.indent = indent
        
        if indent < self.indent:
            self.close()
            return
        
        self._model.add_line(line)

    def close(self):
        self.parent.on_child_close()
    
    def on_child_close(self):
        pass
        
    @property
    def model(self):
        return self._model
        