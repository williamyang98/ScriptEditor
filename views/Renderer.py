from models import Visitor
from .Node import Node
from .Connection import Connection

class Renderer(Visitor):
    def __init__(self, scene):
        self.scene = scene
    
    # conditions
    def visit_condition_block(self, block):
        node = Node("condition_block")
        children = []
        self.scene.addItem(node)
        if block.if_condition:
            children.append(block.if_condition.accept(self))
        for elif_condition in block.elif_conditions:
            children.append(elif_condition.accept(self))
        if block.else_condition:
            children.append(block.else_condition.accept(self))
        for child in children:
            if child:
                connection = Connection(node, child)
                self.scene.addItem(connection)
        return node

    def visit_if_condition(self, con):
        return con.context.accept(self)

    def visit_elif_condition(self, con):
        return con.context.accept(self)

    def visit_else_condition(self, con):
        return con.context.accept(self)

    # context
    def visit_context(self, context):
        node = Node("context")
        self.scene.addItem(node)
        for content in context.contents:
            if isinstance(content, str):
                continue

            child = content.accept(self)
            if child:
                connection = Connection(node, child)
                self.scene.addItem(connection)
        
        return node

    # renpy directives
    def visit_label(self, label):
        node = Node("label: "+label.name)
        self.scene.addItem(node)
        context = label.context.accept(self)
        if context:
            connection = Connection(node, context)
            self.scene.addItem(connection)
        return node
        

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
        node = Node("menu: "+menu.description)
        self.scene.addItem(node)
        for choice in menu.choices:
            child = choice.accept(self)
            if child:
                connection = Connection(node, child)
                self.scene.addItem(connection)
        return node

    def visit_choice(self, choice):
        return choice.context.accept(self)