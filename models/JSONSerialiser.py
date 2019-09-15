from .Visitor import Visitor

class JSONSerialiser(Visitor):
    # conditions
    def visit_condition_block(self, block):
        data = {}
        data["type"] = "condition_block"
        data["if"] = None if not block.if_condition else block.if_condition.accept(self)
        data["elif"] = []
        for elif_condition in block.elif_conditions:
            data["elif"].append(elif_condition.accept(self))
        data["else"] = None if not block.else_condition else block.else_condition.accept(self)

        return data
    
    def visit_if_condition(self, con):
        data = {}
        data["script"] = con.script        
        data["context"] = con.context.accept(self)
        return data
    
    def visit_elif_condition(self, con):
        return self.visit_if_condition(con)
    
    def visit_else_condition(self, con):
        data = {}
        data["context"] = con.context.accept(self)
        return data

    # context
    def visit_context(self, context):
        data = {}
        data["type"] = "context"
        data["children"] = []
        for child in context.children:
            data["children"].append(child.accept(self))
        return data

    # renpy directives
    def visit_label(self, label):
        data = {}
        data["type"] = "label"
        data["name"] = label.name
        data["context"] = label.context.accept(self)

        return data
    
    def visit_jump(self, jump):
        data = {}
        data["type"] = "jump"
        data["label"] = jump.label
        return data

    def visit_call(self, call):
        data = {}
        data["type"] = "call"
        data["label"] = call.label
        return data
    
    def visit_script(self, script):
        data = {}
        data["type"] = "script"
        data["script"] = script.script
        return data
    
    def visit_python_block(self, block):
        data = {}
        data["type"] = "python_block"
        data["lines"] = block.lines
        return data

    # menu
    def visit_menu(self, e):
        data = {}
        data["type"] = "menu"
        data["choices"] = []
        for choice in e.choices:
            data["choices"].append(choice.accept(self))
        return data

    def visit_choice(self, choice):
        data = {}
        data["description"] = choice.description
        data["context"] = choice.context.accept(self)

        return data 
