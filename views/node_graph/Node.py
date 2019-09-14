class Node:
    def __init__(self, view, model, parent=None):
        self.view = view
        self.model = model
        self.parent = parent
        self.children = []

    def addChild(self, node):
        self.children.append(node)
