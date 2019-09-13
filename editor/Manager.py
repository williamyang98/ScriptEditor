from PySide2 import QtGui, QtCore, QtWidgets

from views import Renderer
from .Browser import Browser
from models import JSONSerialiser
from script_parser import parse_lines

import json
import sys
import os

class Manager:
    def __init__(self, organiser, view):
        self.organiser = organiser
        self.view = view
        self.browser = Browser(view) 
        self.renderer = Renderer(organiser, self.browser)
        self.serialiser = JSONSerialiser()
        self.explored_files = {}
    
    def openFile(self, filepath):
        labels = self.cacheFile(filepath)
        if len(labels) > 0:
            self._displayLabels(labels)
    
    def cacheFile(self, filepath):
        if os.path.isdir(filepath):
            return self._loadFromDirectory(filepath)
        elif os.path.isfile(filepath):
            return self._loadFromFile(filepath)
        return []

    def _loadFromDirectory(self, directory):
        labels = []
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isdir(filepath):
                labels.extend(self._loadFromDirectory(filepath))
            else:
                labels.extend(self._loadFromFile(filepath))
        return labels
    
    def _loadFromFile(self, filepath):
        if filepath in self.explored_files:
            return self.explored_files.get(filepath)

        try:
            with open(filepath, "r", encoding="utf8") as fp:
                labels = parse_lines(fp.readlines())
        except:
            labels = []

        self.explored_files.setdefault(filepath, labels)
        return labels        
    
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
    
    def saveModel(self, filepath):
        data = [label.accept(serialiser) for label in self.labels]
        with open(filepath, "w", encoding="utf8") as fp:
            json.dump(data, fp, indent=2)