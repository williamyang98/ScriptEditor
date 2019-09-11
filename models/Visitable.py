from abc import abstractmethod, ABC
from .Visitor import Visitor

class Visitable(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        raise NotImplementedError()