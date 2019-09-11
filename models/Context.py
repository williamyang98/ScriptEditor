class Context:
    def __init__(self):
        self.parent = None
        self.contents = []
    
    def add_content(self, content):
        self.contents.append(content)

class Jump:
    def __init__(self, label):
        self.label = label

class Call:
    def __init__(self, label):
        self.label = label

class Script:
    def __init__(self, script):
        self.script = script

class PythonScript:
    def __init__(self):
        self.lines = []
    
    def add_line(self, line):
        self.lines.append(line)
