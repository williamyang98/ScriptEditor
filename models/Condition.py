from .Visitable import Visitable

class ConditionBlock(Visitable):
    def __init__(self):
        self.if_condition = None
        self.elif_conditions = []
        self.else_condition = None
    
    def add_elif_condition(self, condition):
        self.elif_conditions.append(condition)
    
    def accept(self, visitor):
        return visitor.visit_condition_block(self)

class IfCondition(Visitable):
    def __init__(self, script):
        self.script = script
        self.context = None
    
    def accept(self, visitor):
        return visitor.visit_if_condition(self)
    
class ElifCondition(Visitable):
    def __init__(self, script):
        self.script = script
        self.context = None
    
    def accept(self, visitor):
        return visitor.visit_elif_condition(self)

class ElseCondition(Visitable):
    def __init__(self):
        self.context = None
    
    def accept(self, visitor):
        return visitor.visit_else_condition(self)
