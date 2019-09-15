import os
import json
from script_parser import parse_file
from models import JSONSerialiser

from .NodeTracker import NodeTracker

class LabelsLoader:
    def __init__(self):
        self.nodeTracker = NodeTracker()
        self.serialiser = JSONSerialiser()

        self.nodes = {}
        self.node_filepaths = {}
        self.explored_filepaths = {} 
    
    def getFilepaths(self, id):        
        return self.node_filepaths.get(id)
    
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
        filepath = os.path.normpath(filepath)
        if filepath in self.explored_filepaths:
            return self.explored_filepaths.get(filepath)

        labels = parse_file(filepath)

        for label in labels:
            self._trackNode(label, filepath)

        self.explored_filepaths.setdefault(filepath, labels)
        return labels      
    
    def saveToFile(self, filepath):
        data = [label.accept(serialiser) for label in self.labels.values()]
        with open(filepath, "w", encoding="utf8") as fp:
            json.dump(data, fp, indent=2)
    
    def _trackNode(self, node, filepath):
        id = node.accept(self.nodeTracker)
        if id is not None:
            self.nodes.setdefault(id, node)
            filepaths = self.node_filepaths.setdefault(id, [])
            filepaths.append(filepath)
        for child in node.children:
            self._trackNode(child, filepath)