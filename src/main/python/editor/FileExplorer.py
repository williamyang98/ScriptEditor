from PySide2 import QtGui, QtCore, QtWidgets

class FileExplorer:
    def __init__(self, editor, parent, path="."):
        self.editor = editor

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(path)
        self.model.setNameFilters(["*.rpy"])

        self.tree_view = QtWidgets.QTreeView(parent=parent)
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(path))
        self.tree_view.hideColumn(1)
        self.tree_view.hideColumn(2)
        self.tree_view.hideColumn(3)

        self.tree_view.clicked.connect(self._onClick)
    
    def _onClick(self, index):
        filepath = self.model.filePath(index)
        self.editor.openFile(filepath)
    
    def updateFilepath(self, filepath):
        index = self.model.index(filepath)
        self.tree_view.setCurrentIndex(index)