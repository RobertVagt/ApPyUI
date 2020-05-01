import tkinter as tk


class Canvas(tk.Canvas):
    def __init__(self, master, style=None, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        if style is not None:
            self.config(bg=style.bg)

