from .BaseParser import BaseParser 
from .ParseException import ParseException, FileParseException

def parse_lines(filepath):
    try:
        return parse_filepath(filepath)
    except UnicodeDecodeError as ex:
        return []
    except Exception as ex:
        return []

def parse_filepath(filepath):
    parser = BaseParser()
    with open(filepath, "r", encoding="utf8") as fp:
        for line_number, line in enumerate(fp.readlines()):
            trimmed_line = line.lstrip()
            indent = len(line) - len(trimmed_line)

            if len(trimmed_line) == 0:
                continue
                
            if trimmed_line[0] == '#':
                continue

            try:
                parser.parse_line(indent, line_number, trimmed_line, filepath)
            except ParseException as ex:
                pass
                # raise FileParseException(indent, line_number, line, str(ex))
        
        parser.close()
    return parser.model