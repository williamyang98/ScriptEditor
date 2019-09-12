from PySide2 import QtCore

from models import Visitor
from .Node import Node
from .CubicConnection import CubicConnection

class Renderer(Visitor):
    def __init__(self, scene, organiser):
        self.scene = scene
        self.organiser = organiser
    
    def create_connection(self, start, end):
        connection = CubicConnection(start, end)
        self.scene.addItem(connection)
    
    # conditions
    def visit_condition_block(self, block):
        node = Node("condition_block")
        children = []
        self.scene.addItem(node)
        self.organiser.add_node(node)

        with self.organiser:
            if block.if_condition:
                children.append(block.if_condition.accept(self))
            for elif_condition in block.elif_conditions:
                children.append(elif_condition.accept(self))
            if block.else_condition:
                children.append(block.else_condition.accept(self))

        for child in children:
            if child:
                create_connection(node, child)
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
        self.organiser.add_node(node)
        with self.organiser:
            for content in context.contents:
                if isinstance(content, str):
                    continue
                child = content.accept(self)
                if child:
                    self.create_connection(node, child)
        
        return node

    # renpy directives
    def visit_label(self, label):
        node = Node("label: "+label.name)
        self.scene.addItem(node)
        self.organiser.add_node(node)
        with self.organiser:
            context = label.context.accept(self)

        if context:
            self.create_connection(node, context)

        return node
        

    def visit_jump(self, jump):
        node = Node("jump: "+jump.label)
        self.scene.addItem(node)
        self.organiser.add_node(node)
        return node

    def visit_call(self, call):
        node = Node("call: "+call.label)
        self.scene.addItem(node)
        self.organiser.add_node(node)
        return node

    def visit_script(self, script):
        pass

    def visit_python_block(self, block):
        pass

    # menu
    def visit_menu(self, menu):
        node = Node("menu: {0}".format(menu.description))
        self.scene.addItem(node)
        self.organiser.add_node(node)
        with self.organiser:
            for choice in menu.choices:
                child = choice.accept(self)
                if child:
                    self.create_connection(node, child)

        return node

    def visit_choice(self, choice):
        return choice.context.accept(self)
    

    


