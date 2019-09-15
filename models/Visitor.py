from abc import abstractmethod, ABC

class Visitor(ABC):
    # conditions
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
        pass

    def visit_jump(self, jump):
        pass

    def visit_call(self, call):
        pass

    def visit_script(self, script):
        pass

    def visit_python_block(self, block):
        pass

    # menu
    def visit_menu(self, menu):
        pass

    def visit_choice(self, choice):
        pass

    # text
    def visit_text(self, text):
        pass
