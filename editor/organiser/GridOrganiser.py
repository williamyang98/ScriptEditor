from PySide2 import QtCore
from .Organiser import Organiser

class GridOrganiser(Organiser):
    def __init__(self):
        self.clear()
        self.x_padding = 50
        self.y_padding = 40
        self.position = QtCore.QPoint(0, 0)
    
    def clear(self):
        self.grid = []
        self.column = 0


    # enable context management using enter/exit feature 
    def __enter__(self):
        self.next_column()
        return self
    
    def __exit__(self, type, value, traceback):
        self.previous_column()

    # manually change columns
    def next_column(self):
        self.column += 1
    
    def previous_column(self):
        self.column -= 1
        if self.column < 0:
            self.column = 0

    # add node to current column 
    def add_node(self, node):
        if len(self.grid) <= self.column:
            self.grid.extend([[]]* (self.column-len(self.grid)+1))
        
        current_column = self.grid[self.column]
        current_column.append(node)

    # organise nodes based on parameters
    def organise(self):
        last_x = self.position.x() 
        centre_y = self.position.y() 

        for column in self.grid:
            height = sum((n.boundingRect().height() for n in column))
            width = max((n.boundingRect().width() for n in column))

            height = height + (len(column)-1)*self.y_padding
            centre = height/2

            y = centre_y-centre
            x = last_x

            for node in column:
                node.setPos(QtCore.QPointF(x, y))
                y += node.boundingRect().height()+self.y_padding
            
            last_x = last_x + width + self.x_padding