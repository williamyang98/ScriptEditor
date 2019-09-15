from .Node import Node

class ConditionBlock(Node):
    def __init__(self, metadata):
        super().__init__(metadata)
        self.if_condition = None
        self.elif_conditions = []
        self.else_condition = None
    
    @property
    def children(self):
        children = []
        if self.if_condition:
            children.append(self.if_condition)
        for con in self.elif_conditions:
            children.append(con)
        if self.else_condition:
            children.append(self.else_condition)
        return children
    
    def add_elif_condition(self, condition):
        self.elif_conditions.append(condition)
    
    def accept(self, visitor):
        return visitor.visit_condition_block(self)

class IfCondition(Node):
    def __init__(self, script, metadata):
        super().__init__(metadata)
        self.script = script
        self.context = None
    
    @property
    def children(self):
        if self.context:
            return [self.context]
        return []
    
    def accept(self, visitor):
        return visitor.visit_if_condition(self)
    
class ElifCondition(Node):
    def __init__(self, script, metadata):
        super().__init__(metadata)
        self.script = script
        self.context = None
    
    @property
    def children(self):
        if self.context:
            return [self.context]
        return []

    def accept(self, visitor):
        return visitor.visit_elif_condition(self)

class ElseCondition(Node):
    def __init__(self, metadata):
        super().__init__(metadata)
        self.context = None

    @property
    def children(self):
        if self.context:
            return [self.context]
        return []
    
    def accept(self, visitor):
        return visitor.visit_else_condition(self)
