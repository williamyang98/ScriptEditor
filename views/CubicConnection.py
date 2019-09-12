from PySide2 import QtCore, QtWidgets, QtGui

class CubicConnection(QtWidgets.QGraphicsPathItem):
    def __init__(self, start, end):
        super().__init__()
        self.start = start
        self.end = end

    def paint(self, painter, option, widget):
        self.updatePath()
        super().paint(painter, option, widget)
    
    def updatePath(self):
        start_pos = self.start.mapToScene(self.start.boundingRect().center())
        end_pos = self.end.mapToScene(self.end.boundingRect().center())

        self.setPos(start_pos)

        start = QtCore.QPointF(0, 0)
        end = end_pos-start_pos

        path = QtGui.QPainterPath()
        path.moveTo(start)

        # control points for bezier curve
        # x = midpoint
        # y = top and bottom
        # https://doc.qt.io/qt-5/images/qpainterpath-cubicto.png 
        dx = (end.x() - start.x())/2
        dy = (end.y() - start.y())
        ctrl1 = QtCore.QPointF(start.x()+dx, start.y()) 
        ctrl2 = QtCore.QPointF(start.x()+dx, start.y()+dy) 

        path.cubicTo(ctrl1, ctrl2, end)
        self.setPath(path)


    
