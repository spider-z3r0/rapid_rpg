"""this is a class for the front page"""

from tkinter import *
import tkinter as tk


class FrontPage(tk.Frame):
    """This is a class to make the front page"""
    def __init__(self, master):
        self.master = master
        master.title = "Global Frequency"
        self.input = tk.StringVar()


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
            textvariable = self.input,
            justify = CENTER
        )
        self.name_entry.place(
            relx = 0.5,
            rely = 0.37,
            anchor = 'n'
        )

        self.ent_btn = tk.Button(
            self.mainframe,
            text = "Save",
            font = ("Courier", 15),
            command = lambda: self.getname()
        ).place(
            relx = 0.5,
            rely = 0.43,
            anchor = 'n'
        )

        self.btn_frame = tk.Frame(
            self.mainframe,
            height = 200,
            width = 395,
            bd = 4,
            relief = GROOVE
        ).place(
            relx = 0.5,
            rely = 0.6,
            anchor = 'n'
            
        )

        self.rules_btn = tk.Button(self.mainframe,
            text = "RULES",
            font=("Courier", 15),
        )
        self.rules_btn.place(
            relx = 0.25,
            rely = 0.66,
            anchor = 'n',
            height = 120,
            width = 170
        )

        self.con_btn = tk.Button(self.mainframe,
            text = "DEPLOY",
            font=("Courier", 15),
            justify=CENTER, 
        )
        self.con_btn.place(
            relx = 0.75,
            rely = 0.66,
            anchor = 'n',
            height = 120,
            width = 170
        )

    def getname(self):
        self.input.set(
            self.name_entry.get()
        )








