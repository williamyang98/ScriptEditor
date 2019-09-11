from abc import abstractmethod, ABC

class Visitor(ABC):
    # conditions
    @abstractmethod
    def visit_condition_block(self, o):
        pass

    @abstractmethod
    def visit_if_condition(self, o):
        pass

    @abstractmethod
    def visit_elif_condition(self, o):
        pass

    @abstractmethod
    def visit_else_condition(self, o):
        pass

    # context
    @abstractmethod
    def visit_context(self, o):
        pass

    # renpy directives
    @abstractmethod
    def visit_label(self, o):
        pass

    @abstractmethod
    def visit_jump(self, o):
        pass

    @abstractmethod
    def visit_call(self, o):
        pass

    @abstractmethod
    def visit_script(self, o):
        pass

    @abstractmethod
    def visit_python_block(self, o):
        pass

    # menu
    @abstractmethod
    def visit_menu(self, o):
        pass

    @abstractmethod
    def visit_choice(self, o):
        pass
