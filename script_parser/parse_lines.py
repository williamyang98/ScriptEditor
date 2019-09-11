from .BaseParser import BaseParser 
from .ParseException import ParseException, FileParseException

def parse_lines(lines):
    parser = BaseParser()
    for line_number, line in enumerate(lines):
        trimmed_line = line.lstrip()
        indent = len(line) - len(trimmed_line)

        if len(line) == 0:
            continue
            
        if line[0] == '#':
            continue

        try:
            parser.parse_line(indent, line_number, trimmed_line)
        except ParseException as ex:
            raise FileParseException(indent, line_number, line, str(ex))
    
    parser.close()
    return parser.model