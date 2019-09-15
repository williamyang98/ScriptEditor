from .Parser import Parser
from models import ConditionBlock, IfCondition, ElifCondition, ElseCondition

import re

regex_if   = re.compile(r"if\s+(?P<condition>.*)\s*:")
regex_elif = re.compile(r"elif\s+(?P<condition>.*)\s*:")
regex_else = re.compile(r"else\s*:")

class ConditionParser(Parser):
    def __init__(self, parent, filepath, line_number):
        self.parent = parent
        self._model = ConditionBlock(filepath=filepath, line_number=line_number)
        self.indent = None
        self.condition = None

        self.condition_parser = self.parse_if

        self.child = None
    
    def parse_line(self, indent, line_number, line, filepath):
        if self.indent is None:
            self.indent = indent
        
        if self.child:
            self.child.parse_line(indent, line_number, line, filepath)
            # if child not closed
            if self.child:
                return
        
        if self.condition_parser is None or indent < self.indent:
            self.close()
            return

        # if unable to parse, then end conditional block
        if not self.condition_parser(indent, line_number, line, filepath):
            self.close()
            return
    
    def close(self):
        if self.child:
            self.child.close()
        self.parent.on_child_close()
        
    def on_child_close(self):
        context = self.child.model
        self.condition.context = context
        context.parent = self.condition
        self.condition = None
        self.child = None

    @property
    def model(self):
        return self._model

    def parse_if(self, indent, line_number, line, filepath):
        from .ContextParser import ContextParser
        match = regex_if.match(line)
        if match:
            condition = match["condition"]
            self.child = ContextParser(self, filepath=filepath, line_number=line_number)
            if_condition = IfCondition(condition, filepath=filepath, line_number=line_number)
            self.condition = if_condition
            self._model.if_condition = if_condition

            self.condition_parser = self.parse_elif_or_else
            return True
        return False
    
    def parse_elif(self, indent, line_number, line, filepath):
        from .ContextParser import ContextParser
        match = regex_elif.match(line)
        if match:
            condition = match["condition"]
            self.child = ContextParser(self, filepath=filepath, line_number=line_number)
            elif_condition = ElifCondition(condition, filepath=filepath, line_number=line_number)
            self.condition = elif_condition
            self._model.add_elif_condition(elif_condition)

            self.condition_parser = self.parse_elif_or_else
            return True
        return False
    
    def parse_else(self, indent, line_number, line, filepath):
        from .ContextParser import ContextParser
        match = regex_else.match(line)
        if match:
            self.child = ContextParser(self, filepath=filepath, line_number=line_number)
            else_condition = ElseCondition(filepath=filepath, line_number=line_number)
            self.condition = else_condition
            self._model.else_condition = else_condition

            self.condition_parser = None
            return True
        return False
    
    def parse_elif_or_else(self, indent, line_number, line, filepath):
        return (self.parse_elif(indent, line_number, line, filepath) or \
                self.parse_else(indent, line_number, line, filepath))