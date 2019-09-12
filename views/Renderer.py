from PySide2 import QtCore

from models import Visitor
from .Node import Node
from .Connection import Connection

class Renderer(Visitor):
    def __init__(self, scene):
        self.scene = scene
        self.grid = []
        self.column = 0
    
    # conditions
    def visit_condition_block(self, block):
        node = Node("condition_block")
        children = []
        self.scene.addItem(node)
        self.add_node(node, self.column)
        self.column += 1
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
        self.column -= 1
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
        self.add_node(node, self.column)
        self.column += 1
        for content in context.contents:
            if isinstance(content, str):
                continue

            child = content.accept(self)
            if child:
                connection = Connection(node, child)
                self.scene.addItem(connection)
        
        self.column -= 1
        return node

    # renpy directives
    def visit_label(self, label):
        node = Node("label: "+label.name)
        self.scene.addItem(node)
        self.add_node(node, self.column)
        self.column += 1
        context = label.context.accept(self)
        self.column -= 1
        if context:
            connection = Connection(node, context)
            self.scene.addItem(connection)
        return node
        

    def visit_jump(self, jump):
        node = Node("jump: "+jump.label)
        self.scene.addItem(node)
        self.add_node(node, self.column)
        return node

    def visit_call(self, call):
        node = Node("call: "+call.label)
        self.scene.addItem(node)
        self.add_node(node, self.column)
        return node

    def visit_script(self, script):
        pass

    def visit_python_block(self, block):
        pass

    # menu
    def visit_menu(self, menu):
        node = Node("menu: {0}".format(menu.description))
        self.scene.addItem(node)
        self.add_node(node, self.column)
        self.column += 1
        for choice in menu.choices:
            child = choice.accept(self)
            if child:
                connection = Connection(node, child)
                self.scene.addItem(connection)
        self.column -= 1
        return node

    def visit_choice(self, choice):
        return choice.context.accept(self)
    
    # organise
    def add_node(self, node, column):
        if len(self.grid) <= column:
            self.grid.extend([[]]* (column-len(self.grid)+1))
        
        current_column = self.grid[column]
        current_column.append(node)
    
    def organise(self):
        last_x = 0
        centre_y = 0
        padding = 50

        for column in self.grid:
            height = sum((n.boundingRect().height() for n in column))
            width = max((n.boundingRect().width() for n in column))

            height = height + (len(column)-1)*padding
            centre = height/2

            y = centre_y-centre
            x = last_x

            for node in column:
                node.setPos(QtCore.QPointF(x, y))
                y += node.boundingRect().height()+padding
            
            last_x = last_x + width + padding

