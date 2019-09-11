from abc import abstractmethod, ABC

class Visitor(ABC):
    @abstractmethod
    def visit_condition_block(self, o):
        pass

    @abstractmethod
    def visit_context(self, o):
        pass

    @abstractmethod
    def visit_label(self, e):
        pass

    @abstractmethod
    def visit_menu(self, e):
        pass