from .Node import Node

class Context(Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._children = []

    @property
    def children(self):
        return self._children
    
    def add_child(self, child):
        self._children.append(child)

    def accept(self, visitor):
        return visitor.visit_context(self)

class Jump(Node):
    def __init__(self, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = label
    
    def accept(self, visitor):
        return visitor.visit_jump(self)

class Call(Node):
    def __init__(self, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = label
    
    def accept(self, visitor):
        return visitor.visit_call(self)

class Script(Node):
    def __init__(self, script, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.script = script
    
    def accept(self, visitor):
        return visitor.visit_script(self)
    
    def __str__(self):
        return "SCRIPT {0}".format(self.script)
    
class PythonScript(Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lines = []
    
    def add_line(self, line):
        self.lines.append(line)
    
    def accept(self, visitor):
        return visitor.visit_python_block(self)
    
    def __str__(self):
        return "PYTHON BLOCK"
