from PySide2 import QtCore, QtWidgets, QtGui

class OrganiserControls(QtWidgets.QWidget):
    def __init__(self, parent, organiser):
        super().__init__(parent)
        self.organiser = organiser
    
    def keyPressEvent(self, event):
        print("i hear")
        if event.key() == QtCore.Qt.Key_O:
            self.organiser.organise()

        return super().keyPressEvent(event)
