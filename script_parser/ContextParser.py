import re

from models import Context, Jump, Call, Script, Text
from .Parser import Parser
from .ConditionParser import ConditionParser
from .MenuParser import MenuParser
from .PythonScriptParser import PythonScriptParser

regex_jump = re.compile(r"jump\s+(?P<label>[A-Za-z0-9_\-]+)")
regex_call = re.compile(r"call\s+(?P<label>.+)")
regex_menu = re.compile(r"menu.*:")
regex_condition = re.compile(r"if\s+.+:")
regex_script = re.compile(r"\$\s*(?P<script>.+)")
regex_python_block = re.compile(r"python:")

class ContextParser(Parser):
    def __init__(self, parent, metadata):
        self.parent = parent
        self._model = Context(metadata)
        self.indent = None
        self.child = None
    
    def parse_line(self, metadata):
        if self.indent is None:
            self.indent = metadata.indent

        if self.child is not None:
            self.child.parse_line(metadata)
            if self.child:
                return
        
        if metadata.indent < self.indent:
            self.close()
            return


        match = regex_jump.match(metadata.line)
        if match:
            label = match["label"]
            jump = Jump(label, metadata)
            self._model.add_content(jump)
            return
        
        match = regex_call.match(metadata.line)
        if match:
            label = match["label"]
            call = Call(label, metadata)
            self._model.add_content(call)
            return
        
        match = regex_script.match(metadata.line)
        if match:
            script_code = match["script"]
            script = Script(script_code, metadata)
            self._model.add_content(script)
            return
        
        match = regex_condition.match(metadata.line)
        if match:
            parser = ConditionParser(self, metadata)
            parser.parse_line(metadata)
            self.child = parser
            return
        
        match = regex_menu.match(metadata.line)
        if match:
            parser = MenuParser(self, metadata)
            self.child = parser
            return
        
        match = regex_python_block.match(metadata.line)
        if match:
            parser = PythonScriptParser(self, metadata)
            self.child = parser 
            return
        
        self._model.add_content(Text(metadata.line, metadata))

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
    
