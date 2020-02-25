from .NodeGraphData import NodeGraphData
from .NodeData import NodeData

descriptor = NodeGraphData()

class NodeGraphItem:
    def __init__(self, node, data, parent=None):
        self.node = node
        self.data = data
        self.parent = parent
        self.children = []
    
    def addChild(self, child):
        self.children.append(child)
    
    def childAtRow(self, row):
        if row < 0 or row >= len(self.children):
            return None
        return self.children[row]

    def rowOfChild(self, child):
        return self.children.index(child)

    @property
    def childCount(self):
        return len(self.children)    
    
    @property
    def row(self):
        # if has parent, then get row from it
        if self.parent:
            return self.parent.rowOfChild(self)
        return 0
    
    @property
    def columnCount(self):
        return 1 
    
class BasicNodeGraphItem(NodeGraphItem):
    def __init__(self, node, parent=None):
        super().__init__(node, descriptor.getNodeData(node), parent)
        for child in node.children:
            self.addChild(BasicNodeGraphItem(child, self))

class RootNodeGraphItem(NodeGraphItem):
    def __init__(self, labels):
        super().__init__(None, data=NodeData("Outline"))
        for label in labels:
            self.addChild(BasicNodeGraphItem(label, self))
