from PySide2 import QtCore, QtGui, QtWidgets

INF_WIDTH  = 100000
INF_HEIGHT = 200000

class View(QtWidgets.QGraphicsView):
    def __init__(self, scene, parent):
        super().__init__(scene, parent)
        self._scale = 1.0

        self.isPan = False
        self._lastMousePosition = QtCore.QPoint(0, 0)

        self.scene().setSceneRect(QtCore.QRectF(-INF_WIDTH/2, -INF_HEIGHT/2, INF_WIDTH, INF_HEIGHT))

        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.setInteractive(True)
    
    def zoom(self, zoom, limits=True):
        self._scale = self._scale * zoom
        self.scale(zoom, zoom)

    def setPan(self, isPan):
        self.isPan = isPan
        if isPan:
            self.setCursor(QtCore.Qt.ClosedHandCursor)
        else:
            self.setCursor(QtCore.Qt.ArrowCursor)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MidButton:
            self.setPan(True)
            self._lastMousePosition = event.pos()
        
        return QtWidgets.QGraphicsView.mousePressEvent(self, event)
    
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MidButton:
            self.setPan(False)
        
        return QtWidgets.QGraphicsView.mouseReleaseEvent(self, event)
    
    def mouseMoveEvent(self, event):
        if self.isPan:
            delta = self.mapToScene(event.pos()) - self.mapToScene(self._lastMousePosition)
            self.setTransformationAnchor(QtWidgets.QGraphicsView.NoAnchor);
            self.translate(delta.x(), delta.y())
            self._lastMousePosition = event.pos()

        return QtWidgets.QGraphicsView.mouseMoveEvent(self, event)

    def wheelEvent(self, event):
        delta = event.angleDelta().y() / 8
        zoom = pow(1.25, delta / 100)
        self.zoom(zoom)

    

    

    



