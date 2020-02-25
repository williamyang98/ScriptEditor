from models import Visitor

class ContextDescription(Visitor):
    def visit_call(self, call):
        return ContextData("CALL")

    def visit_jump(self, jump):
        return ContextData("JUMP")

    def visit_menu(self, menu):
        return ContextData("MENU")
    
    def visit_condition_block(self, block):
        return ContextData("CONDITION")
    
    def visit_python_block(self, block):
        return ContextData("PYTHON BLOCK", False)
    
    def visit_text(self, text):
        return ContextData(text.text, False)
    
    def visit_script(self, script):
        return ContextData("SCRIPT {0}".format(script.script), False)

class ContextData:
    def __init__(self, text, hasSocket=True):
        self.text = text
        self.hasSocket = hasSocket