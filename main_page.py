"""The aim here is to prototype the look of the main page"""
from tkinter import *
import tkinter as tk
from character import Character
from dice_roll import Die


class GlobalFrequency:
    """The overall class for the app"""

    def __init__(self, master):
        """intialise the attributes of the variable"""
        self.master = master
        master.title = "Global Frequency"

        # trying to set this up with a character
        self.character = Character("spider jerselem")
        self.character.attributes["Strength"] = tk.IntVar()
        self.character.attributes["Smarts"] = tk.IntVar()
        self.character.attributes["Dexterity"] = tk.IntVar()
        self.character.attributes["Wisdom"] = tk.IntVar()
        self.character.attributes["Charisma"] = tk.IntVar()
        self.character.attributes["Spirit"] = tk.IntVar()

        self.name_label = tk.Label(
            master,
            text=self.character.name.title(),
            font=("Courier", 20),
        )
        self.name_label.pack()

        # This is where the buttons and stuff start
        # Making a dict to store the buttons

        # spirit Buttons and stuff.

        self.spi_frame = tk.Frame(
            master, width=400
        )  # spirit frame
        self.spi_frame.pack(fill=X)

        self.spi_btn_1 = tk.Button(
            self.spi_frame,
            text="Spirit up",
            font=("Courier", 15),
            width=15,
            command=lambda: self.character.increase_attribute(
                "Spirit"
            ),
        )
        self.spi_btn_1.pack(side=LEFT)

        self.spi_btn_2 = tk.Button(
            self.spi_frame,
            text="Spirit down",
            font=("Courier", 15),
            width=15,
            command=lambda: self.character.decrease_attribute(
                "Spirit"
            ),
        )
        self.spi_btn_2.pack(side=LEFT)

        self.spi_label = tk.Label(
            self.spi_frame,
            textvariable=self.character.attributes[
                "Spirit"
            ],
            font=("Courier", 15),
        )
        self.spi_label.pack()

        # making a label to describe the character
        self.character_frame = tk.Frame(
            master, width=400, bd=3
        )
        self.character_frame.pack(fill=X)

        self.character_label = tk.Label(
            self.character_frame,
            text="Activate Attibute",
            font=("Courier", 15),
        )
        self.character_label.pack()

        # setting up check button section
        self.check_frame = tk.Frame(
            master, width=400, bd=3, bg="grey"
        )
        self.check_frame.pack()

        self.st_check = tk.Checkbutton(
            self.check_frame,
            text="Str",
            font=("Courier", 15),
        )  # strength check
        self.st_check.pack(side=LEFT)

        self.sm_check = tk.Checkbutton(
            self.check_frame,
            text="Sma",
            font=("Courier", 15),
        )  # smarts check
        self.sm_check.pack(side=LEFT)

        self.de_check = tk.Checkbutton(
            self.check_frame,
            text="dex",
            font=("Courier", 15),
        )  # dexterity check
        self.de_check.pack(side=LEFT)

        self.wi_check = tk.Checkbutton(
            self.check_frame,
            text="Wis",
            font=("Courier", 15),
        )  # wisdom check
        self.wi_check.pack(side=LEFT)

        self.ca_check = tk.Checkbutton(
            self.check_frame,
            text="Cha",
            font=("Courier", 15),
        )  # charisma check
        self.ca_check.pack(side=LEFT)

        self.sp_check = tk.Checkbutton(
            self.check_frame,
            text="Spi",
            font=("Courier", 15),
        )  # spirit check
        self.sp_check.pack(side=LEFT)

        # trying to make a dice work, the label to print the result is in dice_roll.py
        self.dice_frame = tk.Frame(
            master, width=400, bd=3
        )  # spirit frame
        self.dice_frame.place(
            relx=0.5, rely=0.4, anchor="n"
        )
        self.dice = Die(0, self.dice_frame)
        self.roll_btn = tk.Button(
            self.dice_frame,
            text="Roll 'em",
            font=("Courier", 15),
            width=15,
            command=lambda: self.dice.roll(),
        )
        self.roll_btn.config(relief=SUNKEN)
        self.roll_btn.pack()


root = tk.Tk()
root.geometry("400x600")
gui = GlobalFrequency(root)
root.mainloop()
