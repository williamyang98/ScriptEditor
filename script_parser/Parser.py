from abc import abstractmethod, abstractproperty, ABC

class Parser(ABC):
    @abstractmethod
    def parse_metadata(self, metadata, stack):
        pass
    
    @abstractmethod
    def on_child_pop(self, child):
        pass

    @abstractproperty
    def model(self):
        pass