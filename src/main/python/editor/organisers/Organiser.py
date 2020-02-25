from abc import abstractmethod, ABC

class Organiser(ABC):
    @abstractmethod
    def organise(self, nodeGraph):
        pass
