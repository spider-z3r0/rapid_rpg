"""The aim here is to prototype the look of the main page"""
import tkinter as tk
from character import Character
from dice_roll import Die
from front_page import FrontPage



class GlobalFrequency(tk.Frame):
    """The overall class for the app"""

    def __init__(self, master):
        """intialise the attributes of the variable"""
        self.master = master
        super().__init__(self.master)
        self.input = tk.StringVar()

        master.title = "Global Frequency"
        self.features = {}

        # trying to set this up with a character
        self.character = Character('spider jeruselem')
        self.character.attributes["Strength"] = tk.IntVar()
        self.character.attributes["Strength"].set(1)
        self.character.attributes["Smarts"] = tk.IntVar()
        self.character.attributes["Smarts"].set(1)
        self.character.attributes["Dexterity"] = tk.IntVar()
        self.character.attributes["Dexterity"].set(1)
        self.character.attributes["Wisdom"] = tk.IntVar()
        self.character.attributes["Wisdom"].set(1)
        self.character.attributes["Charisma"] = tk.IntVar()
        self.character.attributes["Charisma"].set(1)
        self.character.attributes["Spirit"] = tk.IntVar()
        self.character.attributes["Spirit"].set(1)

        self.name_label = tk.Label(
            master,
            text=self.character.name.title(),
            font=("Courier", 20),
        )
        self.name_label.pack()

        for key in self.character.attributes:
            self.feature_buttons(key)


                # making a label to describe the character
        self.character_frame = tk.Frame(
            master, width=400, bd=3
        )
        self.character_frame.pack(fill=tk.X)

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
        self.st_check.pack(side=tk.LEFT)

        self.sm_check = tk.Checkbutton(
            self.check_frame,
            text="Sma",
            font=("Courier", 15),
        )  # smarts check
        self.sm_check.pack(side=tk.LEFT)

        self.de_check = tk.Checkbutton(
            self.check_frame,
            text="dex",
            font=("Courier", 15),
        )  # dexterity check
        self.de_check.pack(side=tk.LEFT)

        self.wi_check = tk.Checkbutton(
            self.check_frame,
            text="Wis",
            font=("Courier", 15),
        )  # wisdom check
        self.wi_check.pack(side=tk.LEFT)

        self.ca_check = tk.Checkbutton(
            self.check_frame,
            text="Cha",
            font=("Courier", 15),
        )  # charisma check
        self.ca_check.pack(side=tk.LEFT)

        self.sp_check = tk.Checkbutton(
            self.check_frame,
            text="Spi",
            font=("Courier", 15),
        )  # spirit check
        self.sp_check.pack(side=tk.LEFT)

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
        self.roll_btn.config(relief=tk.SUNKEN)
        self.roll_btn.pack()


    def feature_buttons(self, feature):
        """making buttons"""
        self.features[feature] = {}
        self.features[feature]["frame"] = tk.Frame(
            self.master, 
            width = 400
        )
        self.features[feature]["frame"].pack()
        
        self.features[feature]["increase_button"] = tk.Button(
            self.features[feature]["frame"],
            text=f"{feature} up",
            font=("Courier", 15),
            width=15,
            command=lambda: self.character.increase_attribute(
                    f"{feature}"
                )
            ).pack(side = tk.LEFT)

        self.features[feature]["decrease_button"] = tk.Button(
            self.features[feature]["frame"],
            text=f"{feature} down",
            font=("Courier", 15),
            width=15,
            command=lambda: self.character.decrease_attribute(
                    f"{feature}"
                )
            ).pack(side = tk.LEFT)
        
        self.features[feature]["label"] = tk.Label(
            self.features[feature]["frame"],
             textvariable=self.character.attributes[
                    f"{feature}"
                ],
                font=("Courier", 15),
            ).pack(side = tk.RIGHT)







        




