from .Node import Node

class NodeGraph:
    def __init__(self):
        self.clear()

    def clear(self):
        self.root = Node(None)
        self.root.parent = self.root
        self.parent = self.root
        self.last_node = self.root

    def __enter__(self):
        self.parent = self.last_node
    
    def __exit__(self, *args):
        self.last_node = self.parent
        self.parent = self.last_node.parent
    
    def addView(self, view):
        node = Node(view, self.parent)
        self.last_node = node
        self.parent.addChild(node)
    
