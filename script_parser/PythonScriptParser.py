from .Parser import Parser
from models import PythonScript, Text

class PythonScriptParser(Parser):
    def __init__(self, parent, filepath, line_number):
        self.parent = parent
        self._model = PythonScript(filepath=filepath, line_number=line_number)
        self.indent = None

    def parse_line(self, indent, line_number, line, filepath):
        if self.indent is None:
            self.indent = indent
        
        if indent < self.indent:
            self.close()
            return
        
        self._model.add_line(Text(line, filepath=filepath, line_number=line_number))

    def close(self):
        self.parent.on_child_close()
    
    def on_child_close(self):
        pass
        
    @property
    def model(self):
        return self._model
        