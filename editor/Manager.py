from PySide2 import QtGui, QtCore, QtWidgets

from views import Renderer
from .Browser import Browser
from .LabelsLoader import LabelsLoader

import sys
import os

class Manager:
    def __init__(self, organiser, view):
        self.organiser = organiser
        self.view = view
        self.browser = Browser(self, view) 
        self.renderer = Renderer(organiser, self.browser)
        self.loader = LabelsLoader()
    
    def findExternalLabel(self, label):
        filepath = self.loader.getLabelFilepath(label)
        if filepath:
            self.openFile(filepath)
            self.browser.findLabel(label)
    
    def openFile(self, filepath):
        labels = self.loader.loadFromFilepath(filepath)
        if len(labels) > 0:
            self._displayLabels(labels)
    
    def cacheFile(self, filepath):
        self.loader.loadFromFilepath(filepath) 

    def _displayLabels(self, labels):
        self.clear()
        for label in labels:
            label.accept(self.renderer)
        self.organiseView()
    
    def organiseView(self):
        self.organiser.organise()

    def clear(self):
        self.organiser.clear()
        self.browser.clear()
    
    