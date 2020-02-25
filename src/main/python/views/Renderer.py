from PySide2 import QtCore

from models import Visitor

from .ConditionView import ConditionView
from .context_view import ContextView
from .LabelView import LabelView
from .MenuView import MenuView
from .JumpView import JumpView
from .CallView import CallView
from .CubicConnection import CubicConnection

from .node_graph import NodeGraph

class Renderer(Visitor):
    def __init__(self, scene, editor):
        self.nodeGraph = NodeGraph()
        self.scene = scene
        self.editor = editor
    
    def create_connection(self, start, end):
        connection = CubicConnection(start, end, self.editor)
        self.scene.addItem(connection)
    
    # conditions
    def visit_condition_block(self, block):
        node = ConditionView(block, self.editor)
        self.scene.addItem(node)
        self.nodeGraph.addViewModel(node, block)

        with self.nodeGraph:
            child = block.if_condition.accept(self)
            start = node.getSocket(block.if_condition)
            end = child.getSocket("root")
            self.create_connection(start, end)

            for elif_condition in block.elif_conditions:
                child = elif_condition.accept(self)
                start = node.getSocket(elif_condition)
                end = child.getSocket("root")
                self.create_connection(start, end)

            if block.else_condition:
                child = block.else_condition.accept(self)
                start = node.getSocket(block.else_condition)
                end = child.getSocket("root")
                self.create_connection(start, end)

        return node

    def visit_if_condition(self, con):
        return con.context.accept(self)

    def visit_elif_condition(self, con):
        return con.context.accept(self)

    def visit_else_condition(self, con):
        return con.context.accept(self)

    # context
    def visit_context(self, context):
        node = ContextView(context, self.editor) 
        self.scene.addItem(node)
        self.nodeGraph.addViewModel(node, context)
        with self.nodeGraph:
            for child in context.children:
                childNode = child.accept(self)
                if childNode:
                    start = node.getSocket(child)
                    end = childNode.getSocket("root")
                    self.create_connection(start, end)
        
        return node

    # renpy directives
    def visit_label(self, label):
        node = LabelView(label, self.editor) 
        self.scene.addItem(node)
        self.nodeGraph.addViewModel(node, label)
        with self.nodeGraph:
            context = label.context.accept(self)

        start = node.getSocket("root")
        end = context.getSocket("root")
        self.create_connection(start, end)

        return node
        

    def visit_jump(self, jump):
        node = JumpView(jump, self.editor)
        self.scene.addItem(node)
        self.nodeGraph.addViewModel(node, jump)
        return node

    def visit_call(self, call):
        node = CallView(call, self.editor)
        self.scene.addItem(node)
        self.nodeGraph.addViewModel(node, call)
        return node

    def visit_script(self, script):
        pass

    def visit_python_block(self, block):
        pass

    # menu
    def visit_menu(self, menu):
        node = MenuView(menu, self.editor)
        self.scene.addItem(node)
        self.nodeGraph.addViewModel(node, menu)
        with self.nodeGraph:
            for choice in menu.choices:
                child = choice.accept(self)
                start = node.getSocket(choice)
                end = child.getSocket("root")
                self.create_connection(start, end)

        return node

    def visit_choice(self, choice):
        return choice.context.accept(self)
    

    


