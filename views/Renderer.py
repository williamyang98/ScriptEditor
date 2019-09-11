from models import Visitor
from .Node import Node

class Renderer(Visitor):
    def __init__(self, scene):
        self.scene = scene
    
    # conditions
    def visit_condition_block(self, block):
        self.scene.addItem(Node("condition_block"))
        if block.if_condition:
            block.if_condition.accept(self)
        for elif_condition in block.elif_conditions:
            elif_condition.accept(self)
        if block.else_condition:
            block.else_condition.accept(self)

    def visit_if_condition(self, con):
        con.context.accept(self)

    def visit_elif_condition(self, con):
        con.context.accept(self)

    def visit_else_condition(self, con):
        con.context.accept(self)

    # context
    def visit_context(self, context):
        self.scene.addItem(Node("context"))
        for content in context.contents:
            if isinstance(content, str):
                continue

            content.accept(self)

    # renpy directives
    def visit_label(self, label):
        self.scene.addItem(Node("label: "+label.name))
        label.context.accept(self)
        

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
        self.scene.addItem(Node("menu: "+menu.description))
        for choice in menu.choices:
            choice.accept(self)

    def visit_choice(self, choice):
        choice.context.accept(self)