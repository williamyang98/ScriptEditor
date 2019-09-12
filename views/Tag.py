from PySide2 import QtGui, QtCore, QtWidgets
from .Node import Node
from .Socket import Socket

from abc import abstractproperty

class Tag(Node):
    def __init__(self, left=False):
        super().__init__()
        socket = Socket(self)
        self.addSocket("root", socket)
        self.left = left
        self.x_padding = 10 
        self.y_padding =  5.5 
    
    @abstractproperty
    def tag(self):
        pass
    
    def paint(self, painter, option, widget):
        fontMetrics = painter.fontMetrics()
        width = fontMetrics.width(self.tag)
        height = fontMetrics.height()
        self.width = width + 2*self.x_padding
        self.height = height + 2*self.y_padding

        super().paint(painter, option, widget)

        painter.drawText(
            self.boundingRect(), 
            QtCore.Qt.AlignCenter,
            self.tag)
        
        socket = self.getSocket("root")
        self.alignSocketVCentre(socket)
        if self.left:
            self.alignSocketLeft(socket)
        else:
            self.alignSocketRight(socket)