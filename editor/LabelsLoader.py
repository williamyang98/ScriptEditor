import os
import json
from script_parser import parse_lines
from models import JSONSerialiser

class LabelsLoader:
    def __init__(self):
        self.labels = {}
        self.label_filepaths = {}
        self.explored_filepaths = {} 
        self.serialiser = JSONSerialiser()
    
    def addLabel(self, label, filepath):
        self.labels.setdefault(label.name, label)
        self.label_filepaths.setdefault(label.name, filepath)
        labels = self.explored_filepaths.setdefault(filepath, [])
        if label not in labels: 
            label.append(label)
    
    def getLabel(self, name):
        return self.labels.get(name)
    
    def getLabelFilepath(self, name):        
        return self.label_filepaths.get(name)
    
    def loadFromFilepath(self, filepath):
        if os.path.isdir(filepath):
            return self.loadFromDirectory(filepath)
        elif os.path.isfile(filepath):
            return self.loadFromFile(filepath)
        return []
   
    def loadFromDirectory(self, directory):
        labels = []
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isdir(filepath):
                labels.extend(self.loadFromDirectory(filepath))
            else:
                labels.extend(self.loadFromFile(filepath))
        return labels
    
    def loadFromFile(self, filepath, force=False):
        if filepath in self.explored_filepaths:
            return self.explored_filepaths.get(filepath)

        try:
            with open(filepath, "r", encoding="utf8") as fp:
                labels = parse_lines(fp.readlines())
        except:
            labels = []

        for label in labels:
            self.addLabel(label, filepath)

        return labels      
    
    def saveToFile(self, filepath):
        data = [label.accept(serialiser) for label in self.labels.values()]
        with open(filepath, "w", encoding="utf8") as fp:
            json.dump(data, fp, indent=2)