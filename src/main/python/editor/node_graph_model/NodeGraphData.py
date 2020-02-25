from models import Visitor
from .NodeData import NodeData

# get an id for each possible model for tracker
class NodeGraphData(Visitor):
    def __init__(self, dir="./assets/icons/"):
        self.dir = dir
    
    def getIconPath(self, path):
        return self.dir+path        

    def getNodeData(self, node):
        return node.model.accept(self)

    def visit_condition_block(self, block):
        return NodeData("Condition", self.getIconPath("icon-condition.svg"))

    def visit_if_condition(self, con):
        pass

    def visit_elif_condition(self, con):
        pass

    def visit_else_condition(self, con):
        pass

    # context
    def visit_context(self, context):
        return NodeData("Context", self.getIconPath("icon-context.svg"))

    # renpy directives
    def visit_label(self, label):
        return NodeData("Label {0}".format(label.name), self.getIconPath("icon-label.svg"))

    def visit_jump(self, jump):
        return NodeData("Jump {0}".format(jump.label), self.getIconPath("icon-jump.svg"))

    def visit_call(self, call):
        return NodeData("Call {0}".format(call.label), self.getIconPath("icon-call.svg"))

    def visit_script(self, script):
        pass

    def visit_python_block(self, block):
        pass

    # menu
    def visit_menu(self, menu):
        return NodeData("Menu", self.getIconPath("icon-menu.svg"))

    def visit_choice(self, choice):
        pass