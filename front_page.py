import tkinter as tk





class FrontPage(tk.Frame):
    """This is a class to make the front page
    it inherits from tk.Frame
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.mainframe = tk.Frame(self)
        self.mainframe.pack(expand=True, fill=tk.BOTH)

        self.name_label = tk.Label(
            self.mainframe,
            text="Welcome agent:",
            font=("Courier", 20),
        )
        self.name_label.pack()

        self.inst_label1 = tk.Label(
            self.mainframe,
            text="Agent's name:",
            font=("Courier", 15),
            bd=20,
        )
        self.inst_label1.place(
            relx=0.5, rely=0.3, anchor="n"
        )

        self.name_entry = tk.Entry(
            self.mainframe,
            justify=tk.CENTER,
        )
        self.name_entry.place(
            relx=0.5, rely=0.37, anchor="n"
        )

        self.ent_btn = tk.Button(
            self.mainframe,
            text="Save",
            font=("Courier", 15),
            command= lambda: controller.getname
        )
        self.ent_btn.place(relx=0.5, rely=0.43, anchor="n")

        self.btn_frame = tk.Frame(
            self.mainframe,
            height=200,
            width=395,
            bd=4,
            relief=tk.GROOVE,
        )
        self.btn_frame.place(relx=0.5, rely=0.6, anchor="n")

        self.rules_btn = tk.Button(
            self.mainframe,
            text="RULES",
            font=("Courier", 15),
        )
        self.rules_btn.place(
            relx=0.25,
            rely=0.66,
            anchor="n",
            height=120,
            width=170,
        )

        self.con_btn = tk.Button(
            self.mainframe,
            text="DEPLOY",
            font=("Courier", 15),
            justify=tk.CENTER,
            command = lambda: controller.show_frame("GamePage")
        )
        self.con_btn.place(
            relx=0.75,
            rely=0.66,
            anchor="n",
            height=120,
            width=170,
        )

