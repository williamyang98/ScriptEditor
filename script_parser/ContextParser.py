import re

from models import Context, Jump, Call, Script
from .Parser import Parser
from .ConditionParser import ConditionParser
from .MenuParser import MenuParser
from .PythonScriptParser import PythonScriptParser

regex_jump = re.compile(r"jump\s+(?P<label>[a-z0-9_\-]+)")
regex_menu = re.compile(r"menu.*:")
regex_condition = re.compile(r"if\s+.+:")
regex_script = re.compile(r"\$\s*(?P<script>.+)")
regex_python_block = re.compile(r"python:")

class ContextParser(Parser):
    def __init__(self, parent):
        self.parent = parent
        self._model = Context()
        self.indent = None
        self.child = None
    
    def parse_line(self, indent, line_number, line):
        if self.indent is None:
            self.indent = indent

        if self.child is not None:
            self.child.parse_line(indent, line_number, line)
            if self.child:
                return
        
        if indent < self.indent:
            self.close()
            return


        match = regex_jump.match(line)
        if match:
            label = match["label"]
            jump = Jump(label)
            self._model.add_content(jump)
            return
        
        match = regex_script.match(line)
        if match:
            script_code = match["script"]
            script = Script(script_code)
            self._model.add_content(script)
            return
        
        match = regex_condition.match(line)
        if match:
            parser = ConditionParser(self)
            parser.parse_line(indent, line_number, line)
            self.child = parser
            return
        
        match = regex_menu.match(line)
        if match:
            parser = MenuParser(self)
            self.child = parser
            return
        
        match = regex_python_block.match(line)
        if match:
            parser = PythonScriptParser(self)
            self.child = parser 
            return
        
        self._model.add_content(line)

    def close(self):
        if self.child:
            self.child.close()
        self.parent.on_child_close()
    
    def on_child_close(self):
        sub_model = self.child.model
        self._model.add_content(sub_model)
        self.child = None

    @property
    def model(self):
        return self._model
    
