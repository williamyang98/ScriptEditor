from PySide2 import QtCore
from abc import ABC, abstractmethod, abstractproperty

class TreeOrganiser:
    def __init__(self):
        self.root = Base(QtCore.QPointF(0, 0))
        self.parent = self.root 
        self.last_node = self.root
        self.x_padding = 50
        self.y_padding = 50
    
    def __enter__(self):
        self.parent = self.last_node
    
    def __exit__(self, type, value, traceback):
        self.last_node = self.parent
        self.parent = self.last_node.parent

    def add_node(self, root):
        node = BasicNode(root, self.parent)
        self.last_node = node
        self.parent.addChild(node)
    
    def organise(self):
        self._organise_node(self.root)

    # depth first search
    def _organise_node(self, node):
        # if no children, return
        if len(node.children) == 0:
            node.updateBoundingRect()
            return
        # organise children
        for child in node.children:
            self._organise_node(child)
        # one children are ready, organise this node
        # organise in order of children
        height = sum((c.boundingRect.height() for c in node.children))
        height += (self.y_padding * (len(node.children)-1))
        width = max((c.boundingRect.width() for c in node.children))

        y = node.rootRect.center().y() - height/2
        x = node.rootRect.right() + self.x_padding
        for child in node.children:
            child.position = QtCore.QPointF(x, y)
            y += self.y_padding + child.boundingRect.height()
        # recalculate bounding box
        node.updateBoundingRect()

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

class Base(Node):
    def __init__(self, position):
        super().__init__()
        self._position = position
        self.updateBoundingRect()
    
    @property
    def parent(self):
        return self
    
    @property
    def boundingRect(self):
        return self._boundingRect
    
    @property
    def rootRect(self):
        return QtCore.QRectF(self.position.x(), self.position.y(), 0, 0)
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, pos):
        delta = pos - self.position
        self.translate(delta)

    def translate(self, delta):
        self._position += delta
        self._boundingRect.translate(delta)
        for child in self.children:
            child.translate(delta)

    def updateBoundingRect(self):
        rect = self.rootRect
        if len(self.children) == 0:
            self._boundingRect = rect
            return
        for child in self.children:
            rect = rect.united(child.boundingRect)
        self._boundingRect = rect
        

class BasicNode(Node):
    def __init__(self, root, parent):
        super().__init__()
        self.root = root
        self._parent = parent
        self.updateBoundingRect()
    
    @property
    def parent(self):
        return self._parent

    @property
    def rootRect(self):
        rect = QtCore.QRectF(
            self.root.boundingRect().x(),
            self.root.boundingRect().y(),
            self.root.boundingRect().width(),
            self.root.boundingRect().height())
        rect.moveTo(self.root.pos())
        return rect

    @property
    def boundingRect(self):
        return self._boundingRect
    
    @property
    def position(self):
        return self.boundingRect.topLeft()
    
    @position.setter
    def position(self, pos):
        delta = pos - self.position
        self.translate(delta)

    def translate(self, delta):
        self._boundingRect.translate(delta)
        self.root.setPos(self.root.pos()+delta)
        for child in self.children:
            child.translate(delta)
    
    def updateBoundingRect(self):
        # get initial rect
        rect = self.rootRect
        if len(self.children) == 0:
            self._boundingRect = rect
            return
        # expand rect
        for child in self.children:
            rect = rect.united(child.boundingRect)

        self._boundingRect = rect 





