class ParseException(Exception):
    def __init__(self, message):
        super().__init__(message)

class FileParseException(Exception):
    def __init__(self, indent, lineno, line, msg):
        self.indent = indent
        self.lineno = lineno
        self.line = line
        self.msg = msg
        super().__init__()

    def __str__(self):
        return "line {0}: {1}".format(self.lineno, self.msg)


