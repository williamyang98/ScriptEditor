from .Node import Node

class NodeGraph:
    def __init__(self):
        self.clear()

    def clear(self):
        self.labels = []
        self.parent = None
        self.last_node = None

    def __enter__(self):
        self.parent = self.last_node
    
    def __exit__(self, type, value, traceback):
        if self.parent is None:
            return

        self.last_node = self.parent
        self.parent = self.last_node.parent
    
    def getView(self, id):
        return self.tracked_views.get(id)
    
    def addViewModel(self, view, model):
        node = Node(view, model, self.parent)

        self.last_node = node
        if self.parent is None:
            self.labels.append(node)
        else:
            self.parent.addChild(node)