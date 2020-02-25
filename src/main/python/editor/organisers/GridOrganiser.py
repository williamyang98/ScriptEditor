from PySide2 import QtCore
from .Organiser import Organiser

class GridOrganiser(Organiser):
    def __init__(self):
        self.x_padding = 50
        self.y_padding = 40
        self.position = QtCore.QPoint(0, 0)
    
    # organise nodes based on parameters
    def organise(self, nodeGraph):
        grid = []
        for label in nodeGraph.labels:
            self._populateGrid(grid, label)
        self._organiseGrid(grid)
    
    def _populateGrid(self, grid, node, column=0):
        if len(grid) <= column:
            grid.extend([[]]* (column-len(grid)+1))

        root = node.view
        current_column = grid[column]
        current_column.append(root)

        for child in node.children:
            self._populateGrid(grid, child, column+1)
    
    def _organiseGrid(self, grid):
        last_x = self.position.x() 
        centre_y = self.position.y() 

        for column in grid:
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