from abc import ABC, abstractmethod, abstractproperty

class Node(ABC):
    def __init__(self):
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    @abstractproperty
    def parent(self):
        pass

    @abstractproperty
    def rootRect(self):
        pass

    @abstractproperty
    def boundingRect(self):
        pass

    @abstractproperty
    def position(self):
        pass

    @abstractmethod
    def translate(self):
        pass
    
    @abstractmethod
    def updateBoundingRect(self):
        pass