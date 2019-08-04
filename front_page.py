import tkinter as tk
from main_page import GamePage


class FrontPage(tk.Frame):
    """This is a class to make the front page
    it inherits from tk.Frame
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.mainframe = tk.Frame(self)
        self.mainframe.pack(expand=True, fill=tk.BOTH)

        self.top_label = tk.Label(
            self.mainframe, text="Welcome agent:", font=("Courier", 20)
        )
        self.top_label.pack()

        self.inst_label1 = tk.Label(
            self.mainframe, text="Agent's name:", font=("Courier", 15), bd=20
        )
        self.inst_label1.place(relx=0.5, rely=0.3, anchor="n")

        self.v = tk.StringVar()

        self.name_entry = tk.Entry(
            self.mainframe, textvariable=self.v.get().title(), justify=tk.CENTER
        )
        self.name_entry.place(relx=0.5, rely=0.37, anchor="n")

        self.ent_btn = tk.Button(
            self.mainframe, text="Save", font=("Courier", 15), command=self.on_button
        )
        self.ent_btn.place(relx=0.5, rely=0.43, anchor="n")

        self.output_frame = tk.Label(
            self.mainframe,
            text="Please enter your codename below",
            font=("Courier", 15),
            bd=0,
            relief=tk.GROOVE,
        )
        self.output_frame.pack()

        self.btn_frame = tk.Frame(
            self.mainframe, height=200, width=395, bd=4, relief=tk.GROOVE
        )
        self.btn_frame.place(relx=0.5, rely=0.6, anchor="n")

        self.rules_btn = tk.Button(self.mainframe, text="RULES", font=("Courier", 15))
        self.rules_btn.place(relx=0.25, rely=0.66, anchor="n", height=120, width=170)

        self.con_btn = tk.Button(
            self.mainframe,
            text="DEPLOY",
            font=("Courier", 15),
            justify=tk.CENTER,
            command=lambda: controller.show_frame("GamePage"),
        )

        self.con_btn.place(relx=0.75, rely=0.66, anchor="n", height=120, width=170)

    def on_button(self):
        self.v.set(self.name_entry.get())
