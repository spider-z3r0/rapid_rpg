import tkinter as tk



class SecondPage(tk.Frame):
    """This is a class to make the second page
    it inherits from tk.Frame
    """

    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.input = tk.StringVar()

        self.mainframe = tk.Frame(self)
        self.mainframe.pack(expand=True, fill=tk.BOTH)

        self.label = tk.Label(
            self.mainframe, text="second page"
        )
        self.label.pack()