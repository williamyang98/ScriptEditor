from models import Visitor

# get an id for each possible model for tracker
class NodeDescriptions(Visitor):
    def getNodeDescription(self, node):
        return node.model.accept(self)

    def visit_condition_block(self, block):
        return "Condition"

    def visit_if_condition(self, con):
        pass

    def visit_elif_condition(self, con):
        pass

    def visit_else_condition(self, con):
        pass

    # context
    def visit_context(self, context):
        return "Context"

    # renpy directives
    def visit_label(self, label):
        return "Label {0}".format(label.name)

    def visit_jump(self, jump):
        return "Jump {0}".format(jump.label)

    def visit_call(self, call):
        return "Call {0}".format(call.label)

    def visit_script(self, script):
        pass

    def visit_python_block(self, block):
        pass

    # menu
    def visit_menu(self, menu):
        return "Menu"

    def visit_choice(self, choice):
        pass