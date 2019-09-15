from models import MetaData

from .ParserStack import ParserStack
from .ParseException import ParseException, FileParseException

def parse_file(filepath):
    parser = ParserStack()

    try:
        for metadata in get_metadata(filepath):
            try:
                parser.parse_metadata(metadata)
            except ParseException as ex:
                pass
    except UnicodeDecodeError as ex:
        pass

    parser.collapse()
    labels = parser.labels
    return labels

def get_metadata(filepath):
    with open(filepath, "r", encoding="utf8") as fp:
        for line_number, line in enumerate(fp.readlines()):
            trimmed_line = line.lstrip()
            indent = len(line) - len(trimmed_line)

            if len(trimmed_line) == 0:
                continue
                
            if trimmed_line[0] == '#':
                continue
                
            metadata = MetaData(indent, line_number, filepath, trimmed_line)
            yield metadata
