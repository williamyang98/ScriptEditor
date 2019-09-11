from .Visitable import Visitable

class Context(Visitable):
    def __init__(self):
        self.parent = None
        self.contents = []
    
    def add_content(self, content):
        self.contents.append(content)

    def accept(self, visitor):
        return visitor.visit_context(self)

class Jump(Visitable):
    def __init__(self, label):
        self.label = label
    
    def accept(self, visitor):
        return visitor.visit_jump(self)

class Call(Visitable):
    def __init__(self, label):
        self.label = label
    
    def accept(self, visitor):
        return visitor.visit_call(self)

class Script(Visitable):
    def __init__(self, script):
        self.script = script
    
    def accept(self, visitor):
        return visitor.visit_script(self)

class PythonScript(Visitable):
    def __init__(self):
        self.lines = []
    
    def add_line(self, line):
        self.lines.append(line)
    
    def accept(self, visitor):
        return visitor.visit_python_block(self)
