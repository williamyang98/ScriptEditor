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
        self.context = Context(metadata)
        self.indent = None
    
    def parse_metadata(self, metadata, stack):
        if self.indent is None:
            self.indent = metadata.indent

        if metadata.indent < self.indent:
            self.close(metadata, stack)
            return

        match = regex_jump.match(metadata.line)
        if match:
            label = match["label"]
            jump = Jump(label, metadata)
            self.context.add_child(jump)
            return
        
        match = regex_call.match(metadata.line)
        if match:
            label = match["label"]
            call = Call(label, metadata)
            self.context.add_child(call)
            return
        
        match = regex_script.match(metadata.line)
        if match:
            script_code = match["script"]
            script = Script(script_code, metadata)
            self.context.add_child(script)
            return
        
        match = regex_condition.match(metadata.line)
        if match:
            parser = ConditionParser(self, metadata)
            stack.push(parser)
            stack.parse_metadata(metadata)
            return
        
        match = regex_menu.match(metadata.line)
        if match:
            parser = MenuParser(self, metadata)
            stack.push(parser)
            return
        
        match = regex_python_block.match(metadata.line)
        if match:
            parser = PythonScriptParser(self, metadata)
            stack.push(parser)
            return
        
        self.context.add_child(Text(metadata.line, metadata))

    def close(self, metadata, stack):
        stack.pop()
        stack.parse_metadata(metadata)
    
    def on_child_pop(self, child):
        self.context.add_child(child.model)

    @property
    def model(self):
        return self.context
    
