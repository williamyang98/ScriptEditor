from PySide2 import QtGui, QtCore, QtWidgets

from views import Renderer
from .Browser import Browser
from models import JSONSerialiser
from script_parser import parse_lines

import json
import sys
import os

class Manager:
    def __init__(self, organiser, scene):
        self.organiser = organiser
        self.scene = scene
        self.browser = Browser() 
        self.renderer = Renderer(scene, organiser, self.browser)
        self.serialiser = JSONSerialiser()
        self.labels = []
    
    def loadFromFile(self, filepath):
        self.clear()

        with open(filepath, "r", encoding="utf8") as fp:
            self.labels = parse_lines(fp.readlines())
        
        for label in self.labels:
            label.accept(self.renderer)

        self.organiseView() 
    
    def organiseView(self):
        self.organiser.organise()

    def clear(self):
        self.organiser.clear()
        self.scene.clear()
    
    def saveModel(self, filepath):
        data = [label.accept(serialiser) for label in self.labels]
        with open(filepath, "w", encoding="utf8") as fp:
            json.dump(data, fp, indent=2)