from PySide2 import QtGui, QtCore, QtWidgets
from .NodeGraphItem import NodeGraphItem, RootNodeGraphItem

# convert from nodegraph to qmodel

class NodeGraphModel(QtCore.QAbstractItemModel):
    def __init__(self, labels, parent=None):
        super().__init__(parent)
        self.viewCache = {}
        self.indexCache = {}
        self.rootItem = RootNodeGraphItem(labels)    
        self._cacheNodeModel(self.rootItem)
    
    def getNodeFromView(self, view):
        return self.viewCache.get(view)
    
    def getIndexFromNode(self, node):
        return self.indexCache.get(node)
    
    def getNodeFromIndex(self, index):
        if not index.isValid():
            return None
        
        item = index.internalPointer()
        return item.node
    
    def _cacheNodeModel(self, nodeModel):
        node = nodeModel.node
        if node and node.view:
            self.viewCache.setdefault(node.view, nodeModel)
        for childModel in nodeModel.children:
            self._cacheNodeModel(childModel)

    def createIndex(self, row, column, item):
        index = super().createIndex(row, column, item)
        self.indexCache.setdefault(item, index)
        return index
        
    def index(self, row, column, parent):
        # index is invalid
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()
        # bad parent, set as base root 
        if not parent.isValid():
            parentItem = self.rootItem
        # otherwise set as internal pointer (QT)
        else:
            parentItem = parent.internalPointer()

        # set child item as the index 
        childItem = parentItem.childAtRow(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QtCore.QModelIndex()

    # get index of the parent
    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()
        
        childItem = index.internalPointer()
        parentItem = childItem.parent

        if childItem == self.rootItem or parentItem is None:
            return QtCore.QModelIndex()
        
        return self.createIndex(parentItem.row, 0, parentItem)
    
    def rowCount(self, parent):
        if parent.column() > 0:
            return 0
        
        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()
        
        return parentItem.childCount
    
    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount
        return self.rootItem.columnCount
    
    def data(self, index, role):
        if not index.isValid():
            return None
        
        if role != QtCore.Qt.DisplayRole:
            return None
        
        item = index.internalPointer()
        return item.getData(index.column())
    
    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags
        return super().flags(index)
    
    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootItem.getData(section)
        return None




        

        