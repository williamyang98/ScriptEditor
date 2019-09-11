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

class IfCondition:
    def __init__(self, script):
        self.script = script
        self.context = None

    def __str__(self):
        return "If {0}".format(self.script)
    
class ElifCondition:
    def __init__(self, script):
        self.script = script
        self.context = None

    def __str__(self):
        return "Elif {0}".format(self.script)

class ElseCondition:
    def __init__(self):
        self.context = None

    def __str__(self):
        return "Else"

