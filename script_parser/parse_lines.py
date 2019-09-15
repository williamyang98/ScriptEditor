from models import MetaData

from .ParserStack import ParserStack
from .ParseException import ParseException, FileParseException

def parse_lines(filepath):
    try:
        return parse_filepath(filepath)
    except UnicodeDecodeError as ex:
        return []

def parse_filepath(filepath):
    parser = ParserStack()
    with open(filepath, "r", encoding="utf8") as fp:
        for line_number, line in enumerate(fp.readlines()):
            trimmed_line = line.lstrip()
            indent = len(line) - len(trimmed_line)

            if len(trimmed_line) == 0:
                continue
                
            if trimmed_line[0] == '#':
                continue

            try:
                metadata = MetaData(indent, line_number, filepath, trimmed_line)
                parser.parse_metadata(metadata)
            except ParseException as ex:
                pass
                # raise FileParseException(indent, line_number, line, str(ex))

    parser.collapse()
    labels = parser.base.labels
    return labels