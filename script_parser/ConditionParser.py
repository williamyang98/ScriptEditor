from .Parser import Parser
from models import ConditionBlock, IfCondition, ElifCondition, ElseCondition

import re

regex_if   = re.compile(r"if\s+(?P<condition>.*)\s*:")
regex_elif = re.compile(r"elif\s+(?P<condition>.*)\s*:")
regex_else = re.compile(r"else\s*:")

class ConditionParser(Parser):
    def __init__(self, parent, metadata):
        self.parent = parent
        self._model = ConditionBlock(metadata)
        self.indent = None
        self.condition = None

        self.condition_parser = self.parse_if

        self.child = None
    
    def parse_line(self, metadata):
        if self.indent is None:
            self.indent = metadata.indent
        
        if self.child:
            self.child.parse_line(metadata)
            # if child not closed
            if self.child:
                return
        
        if self.condition_parser is None or metadata.indent < self.indent:
            self.close()
            return

        # if unable to parse, then end conditional block
        if not self.condition_parser(metadata):
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

    def parse_if(self, metadata):
        from .ContextParser import ContextParser
        match = regex_if.match(metadata.line)
        if match:
            condition = match["condition"]
            self.child = ContextParser(self, metadata)
            if_condition = IfCondition(condition, metadata)
            self.condition = if_condition
            self._model.if_condition = if_condition

            self.condition_parser = self.parse_elif_or_else
            return True
        return False
    
    def parse_elif(self, metadata):
        from .ContextParser import ContextParser
        match = regex_elif.match(metadata.line)
        if match:
            condition = match["condition"]
            self.child = ContextParser(self, metadata)
            elif_condition = ElifCondition(condition, metadata)
            self.condition = elif_condition
            self._model.add_elif_condition(elif_condition)

            self.condition_parser = self.parse_elif_or_else
            return True
        return False
    
    def parse_else(self, metadata):
        from .ContextParser import ContextParser
        match = regex_else.match(metadata.line)
        if match:
            self.child = ContextParser(self, metadata)
            else_condition = ElseCondition(metadata)
            self.condition = else_condition
            self._model.else_condition = else_condition

            self.condition_parser = None
            return True
        return False
    
    def parse_elif_or_else(self, metadata):
        return (self.parse_elif(metadata) or \
                self.parse_else(metadata))