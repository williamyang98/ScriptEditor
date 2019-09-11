from abc import abstractmethod, abstractproperty, ABC

class Parser(ABC):
    @abstractmethod
    def parse_line(self, indent, line_number, line):
        raise NotImplementedError()
    
    @abstractmethod
    def close(self):
        raise NotImplementedError()

    @abstractmethod
    def on_child_close(self):
        raise NotImplementedError()

    def model(self):
        raise NotImplementedError()