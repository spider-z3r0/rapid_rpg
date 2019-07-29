import tkinter as tk
from front_page import FrontPage
from main_page import GlobalFrequency


class GUI(tk.Tk):
    """this is the app
    it inherits from tk.Tk
    """

    def __init__(self):
        super().__init__()
        self.title = "Global Frequency"
        self.geometry("400x600")

        self.navig_frame = tk.Frame(self)
        self.first_btn = tk.Button(
            self.navig_frame,
            text="show_first",
            command=self.show_first,
        )
        self.first_btn.pack(side=tk.LEFT)
        self.second_btn = tk.Button(
            self.navig_frame,
            text="show_second",
            command=self.show_second,
        )
        self.second_btn.pack(side=tk.LEFT)

        self.navig_frame.pack()


        self.front = FrontPage(self)
        self.front.pack(expand=True, fill=tk.BOTH)

        self.second = GlobalFrequency(self)

    def show_first(self):
        self.second.pack_forget()
        self.front.pack(expand=True, fill=tk.BOTH)

    def show_second(self):
        self.front.pack_forget()
        self.second.pack(expand=True, fill=tk.BOTH)


gui = GUI()
gui.mainloop()