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

    def center(toplevel):
        toplevel.update_idletasks()

        # Tkinter way to find the screen resolution
        # screen_width = toplevel.winfo_screenwidth()
        # screen_height = toplevel.winfo_screenheight()

        # PyQt way to find the screen resolution
        app = QtGui.QApplication([])
        screen_width = app.desktop().screenGeometry().width()
        screen_height = app.desktop().screenGeometry().height()

        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = screen_width/2 - size[0]/2
        y = screen_height/2 - size[1]/2

        toplevel.geometry("+%d+%d" % (x, y))
        toplevel.title("Centered!")

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
