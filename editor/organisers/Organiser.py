from abc import abstractmethod, ABC

class Organiser(ABC):
    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, type, value, traceback):
        pass

    @abstractmethod
    def add_node(self, node):
        pass

    @abstractmethod
    def organise(self):
        pass
