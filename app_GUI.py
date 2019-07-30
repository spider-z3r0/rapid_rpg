import tkinter as tk
import front_page
import main_page


class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        # Initialize Window
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.name = tk.StringVar()

        self.frames = {}
        for F in (front_page.FrontPage,main_page.GamePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("FrontPage")




    # shows the desired frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        return True

    def getname(self):
        self.name.set(self.frames[front_page.FrontPage].name_entry.get())
        print(self.name.get())






app = GUI()
app.geometry("400x600")
app.mainloop()



