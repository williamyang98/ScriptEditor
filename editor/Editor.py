from PySide2 import QtGui, QtCore, QtWidgets
from .Manager import Manager
from .View import View
from .organisers import TreeOrganiser, GridOrganiser

class Editor:
    def __init__(self, rootPath="."):
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setWindowTitle("Nodal editor")

        self._createFileExplorer(rootPath)

        self.scene = QtWidgets.QGraphicsScene()
        self.view = View(self.scene, parent=self.splitter)

        self.organiser = TreeOrganiser()
        self.manager = Manager(self.organiser, self.view)
        self.manager.cacheFile(rootPath)

        def dummy(index):
            filepath = self.model.filePath(index)
            self.manager.openFile(filepath)


        self.tree_view.clicked.connect(dummy)
    
    def show(self):
        self.splitter.show()
    
    def _createFileExplorer(self, path):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(path)
        self.model.setNameFilters(["*.rpy"])

        self.tree_view = QtWidgets.QTreeView(parent=self.splitter)
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(path))
