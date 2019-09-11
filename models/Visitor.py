from abc import abstractmethod, ABC

class Visitor(ABC):
    # conditions
    @abstractmethod
    def visit_condition_block(self, block):
        pass

    @abstractmethod
    def visit_if_condition(self, con):
        pass

    @abstractmethod
    def visit_elif_condition(self, con):
        pass

    @abstractmethod
    def visit_else_condition(self, con):
        pass

    # context
    @abstractmethod
    def visit_context(self, context):
        pass

    # renpy directives
    @abstractmethod
    def visit_label(self, label):
        pass

    @abstractmethod
    def visit_jump(self, jump):
        pass

    @abstractmethod
    def visit_call(self, call):
        pass

    @abstractmethod
    def visit_script(self, script):
        pass

    @abstractmethod
    def visit_python_block(self, block):
        pass

    # menu
    @abstractmethod
    def visit_menu(self, menu):
        pass

    @abstractmethod
    def visit_choice(self, choice):
        pass
