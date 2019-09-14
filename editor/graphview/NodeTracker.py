from models import Visitor

# get an id for each possible model for tracker
class NodeTracker(Visitor):
    def __init__(self, nodeGraph):
        self.tracked_views = {}
        for label in nodeGraph.labels:
            self._trackNode(label)

    def _trackNode(self, node):
        id = node.model.accept(self)
        if id is not None:
            self.tracked_views.setdefault(id, node.view)
        for child in node.children:
            self._trackNode(child)

    def getView(self, id):
        return self.tracked_views.get(id)

    def visit_condition_block(self, block):
        pass

    def visit_if_condition(self, con):
        pass

    def visit_elif_condition(self, con):
        pass

    def visit_else_condition(self, con):
        pass

    # context
    def visit_context(self, context):
        pass

    # renpy directives
    def visit_label(self, label):
        return "label {0}".format(label.name)

    def visit_jump(self, jump):
        return "jump {0}".format(jump.label)

    def visit_call(self, call):
        return "call {0}".format(call.label)

    def visit_script(self, script):
        pass

    def visit_python_block(self, block):
        pass

    # menu
    def visit_menu(self, menu):
        pass

    def visit_choice(self, choice):
        pass
