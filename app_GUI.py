import tkinter as tk
import front_page


class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        # Initialize Window
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        pages = [front_page.FrontPage]
        # Load all pages
        for F in pages:
            frame = F(container, self, pages)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(front_page.FrontPage)

        self.show_frame(front_page.FrontPage)

    # shows the desired frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        return True

    # passes text to the window StartPage
    def pass_on_text(self, text):
        self.frames[StartPage].get_text(text)


app = GUI()
app.geometry("400x600")
app.mainloop()
