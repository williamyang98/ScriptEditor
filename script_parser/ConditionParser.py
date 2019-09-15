from .Parser import Parser
from models import ConditionBlock, IfCondition, ElifCondition, ElseCondition

import re

regex_if   = re.compile(r"if\s+(?P<condition>.*)\s*:")
regex_elif = re.compile(r"elif\s+(?P<condition>.*)\s*:")
regex_else = re.compile(r"else\s*:")

class ConditionParser(Parser):
    def __init__(self, parent, metadata):
        self.parent = parent
        self.block = ConditionBlock(metadata)
        self.indent = None
        self.condition = None

        self.condition_parser = self.parse_if

    def parse_metadata(self, metadata, stack):
        from .ContextParser import ContextParser
        if self.indent is None:
            self.indent = metadata.indent
        
        if self.condition_parser is None or metadata.indent < self.indent:
            self.close(metadata, stack)
            return

        # if unable to parse, then end conditional block
        if self.condition_parser(metadata, stack):
            parser = ContextParser(self.block, metadata)
            stack.push(parser)
        else:
            self.close(metadata, stack)
        
    def on_child_pop(self, child):
        self.condition.context = child.model
    
    def close(self, metadata, stack):
        stack.pop()
        stack.parse_metadata(metadata)
        
    @property
    def model(self):
        return self.block

    def parse_if(self, metadata, stack):
        from .ContextParser import ContextParser
        match = regex_if.match(metadata.line)
        if match:
            condition = match["condition"]
            if_condition = IfCondition(condition, metadata)
            self.condition = if_condition
            self.block.if_condition = if_condition
            self.condition_parser = self.parse_elif_or_else
            return True
        return False
    
    def parse_elif(self, metadata, stack):
        from .ContextParser import ContextParser
        match = regex_elif.match(metadata.line)
        if match:
            condition = match["condition"]
            elif_condition = ElifCondition(condition, metadata)
            self.condition = elif_condition
            self.block.add_elif_condition(elif_condition)
            self.condition_parser = self.parse_elif_or_else
            return True
        return False
    
    def parse_else(self, metadata, stack):
        from .ContextParser import ContextParser
        match = regex_else.match(metadata.line)
        if match:
            else_condition = ElseCondition(metadata)
            self.condition = else_condition
            self.block.else_condition = else_condition
            self.condition_parser = None
            return True
        return False
    
    def parse_elif_or_else(self, metadata, stack):
        return (self.parse_elif(metadata, stack) or \
                self.parse_else(metadata, stack))