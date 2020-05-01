import tkinter as tk
import tkinter.ttk as ttk

from appyui.guielements import Canvas
from appyui.helpers import Dispatcher


class Model(Dispatcher):
    def __init__(self):
        Dispatcher.__init__(self)


class Controller(Dispatcher):
    def __init__(self, model, view):
        Dispatcher.__init__(self)
        self.model = model
        self.view = view
        self.sub_controllers = []

        self.model.add_listener(self)
        self.view.add_listener(self)

    def add_sub_controller(self, sub_con):
        self.sub_controllers.append(sub_con)


# inherits from canvas
class View(Dispatcher, Canvas):
    def __init__(self, master, *args, **kwargs):
        Dispatcher.__init__(self)
        Canvas.__init__(self, master, *args, **kwargs)


class App:
    def __init__(self):
        pass

