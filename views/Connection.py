from PySide2 import QtGui, QtCore, QtWidgets

class Connection(QtWidgets.QGraphicsItem):
    def __init__(self, start, end):
        super().__init__()
        self.start = start
        self.end = end
        self.update()
    
    def update(self):
        super().update()

        start_pos = self.start.mapToScene(self.start.boundingRect().center())
        end_pos = self.end.mapToScene(self.end.boundingRect().center())

        self.setPos(start_pos)

        start = QtCore.QPointF(0, 0)
        end = end_pos-start_pos
        line = QtCore.QLineF(start, end)

        normal = line.unitVector().normalVector() # normal for width
        normal = 2 *  QtCore.QPointF(
            normal.x2()-normal.x1(),
            normal.y2()-normal.y1())

        shape = QtGui.QPainterPath()
        rect = QtGui.QPolygonF([
            start-normal, 
            start+normal, 
            end+normal, 
            end-normal])
        
        shape.addPolygon(rect)
        shape.closeSubpath()

        self._line = line
        self._shape = shape
    
    def shape(self):
        return self._shape
    
    def boundingRect(self):
        return self._shape.controlPointRect()
    
    def paint(self, painter, option, widget):
        self.update()
        palette = self.scene().palette()
        brush = palette.text()
        
        painter.setPen(QtGui.QPen(brush, 2.0))
        painter.drawLine(self._line)





