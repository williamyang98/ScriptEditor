class Node:
    def __init__(self, view, parent=None):
        self.view = view
        self.parent = parent
        self.children = []

    def addChild(self, node):
        self.children.append(node)
