class Browser:
    def __init__(self):
        self.labels = {}

    def addLabel(self, label, view):
        self.labels.setdefault(label, view)

    def findLabel(self, label):
        view = self.labels.get(label)
        if view is not None:
            print("goto {0}".format(label))
            self.centreOn(view.pos())

    def centreOn(self, position):
        print("centre to {0}".format(position.x(), position.y()))