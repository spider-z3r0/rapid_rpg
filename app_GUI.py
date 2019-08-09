"""This is the main app, all other frames and the significant funtions"""

import tkinter as tk


# Importing the other pages from the app.
from front_page import FrontPage
from main_page import GamePage


class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        # Initialize Window
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FrontPage, GamePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("FrontPage")

    def show_frame(self, page_name):
        """Shows the desired frame"""
        frame = self.frames[page_name]
        frame.tkraise()

    def get_page(self, page_name):
        """allows you to create a reference to other pages"""
        return self.frames[page_name]


app = GUI()
app.geometry("400x600")
app.mainloop()
