from abc import abstractmethod, ABC

class Visitable(ABC):
    @abstractmethod
    def accept(self, visitor):
        raise NotImplementedError()