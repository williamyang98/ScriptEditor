from PySide2 import QtGui, QtCore, QtWidgets
from .graphview import GraphView

class FileTabs(QtWidgets.QTabWidget):
    def __init__(self, editor, parent):
        super().__init__(parent=parent)
        self.editor = editor
        self.tabs = self # TODO: Decouple into a widget as composite
        self.tabs.setTabsClosable(True)
        self.openedFiles = {}

        self.currentChanged.connect(self._onTabChange)
        self.tabCloseRequested.connect(self._onTabClose)

    def openLabels(self, labels, filepath):
        if filepath in self.openedFiles:
            index = self.openedFiles.get(filepath)
            self.tabs.setCurrentIndex(index)
            return

        graphView = GraphView(editor=self.editor, parent=self.tabs)
        graphView.open(labels)
        index = self.tabs.addTab(graphView, filepath)
        self.openedFiles.setdefault(filepath, index)
        self.tabs.setCurrentIndex(index)
    
    def getCurrentGraphScene(self):
        index = self.tabs.currentIndex()
        graphView = self.tabs.widget(index)
        return graphView

    def _onTabChange(self, index=None):
        self.editor.updateGraphScene()
    
    def _onTabClose(self, index):
        self.tabs.removeTab(index)
        key = None
        for _key, _index in self.openedFiles.items():
            if _index == index:
                key = _key
                break
        if key is not None:
            self.openedFiles.pop(key)
            self.editor.updateGraphScene()