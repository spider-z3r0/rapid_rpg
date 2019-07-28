"""this is a class for the front page"""

from tkinter import *
import tkinter as tk


class FrontPage:
    """This is a class to make the front page"""
    def __init__(self, master):
        self.master = master
        master.title = "Global Frequency"


        self.mainframe = tk.Frame(
            master
        ).pack()

        self.name_label = tk.Label(
            self.mainframe,
            text="Welcome agent:",
            font=("Courier", 20),
        )
        self.name_label.pack()

        self.inst_label1 = tk.Label(
            self.mainframe,
            text = "Agent's name:", 
            font = ("Courier", 15),
            bd = 20,
        )
        self.inst_label1.place(
            relx = 0.5,
            rely = 0.3,             
            anchor = 'n'
        )


        self.name_entry = tk.Entry(
            self.mainframe,
            justify = CENTER
        ).place(
            relx = 0.5,
            rely = 0.37,
            anchor = 'n'
        )



root = tk.Tk()
root.geometry("400x600")
gui = FrontPage(root)
root.mainloop()

