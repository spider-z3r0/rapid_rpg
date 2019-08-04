"""The aim here is to prototype the look of the main page"""
import tkinter as tk
from tkinter import SUNKEN
from character import Character
import random
import itertools



class GamePage(tk.Frame):
    """The overall class for the app"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.features = {}
        self.atts = ["Str", "Sma", "Dex", "Wiz", "Cha", "Spi"]
        self.att_buttons = {}

        front_page = self.controller.get_page("FrontPage")
        self.character_name = front_page.v

        self.mainframe = tk.Frame(self)
        self.mainframe.pack(expand=True, fill=tk.BOTH)

        # trying to set this up with a character
        self.character = Character()
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
            self.mainframe,
            textvariable=front_page.v,
            font=("Courier", 20),
            bd=1,
            relief=SUNKEN,
        )
        self.name_label.pack()

        st_var = tk.BooleanVar()
        sm_var = tk.BooleanVar()
        de_var = tk.BooleanVar()
        wi_var = tk.BooleanVar()
        ch_var = tk.BooleanVar()
        sp_var = tk.BooleanVar()
        self.v_list = [st_var, sm_var, de_var, wi_var, ch_var, sp_var]

        # setting up check button section
        self.check_frame = tk.Frame(self.mainframe, width=400, bd=3, bg="grey")
        self.check_frame.place(relx=0.5, rely=0.34, anchor="n")

        for key in self.character.attributes:
            self.feature_buttons(key)

        for (i, j) in zip(self.atts, self.v_list):
            self.att_buttons[i] = {}
            self.att_buttons[i]["checkbutton"] = tk.Checkbutton(
                self.check_frame, text=i, font=("Courier", 15),
                variable = j 
            )
            self.att_buttons[i]["checkbutton"].pack(side=tk.LEFT)


        # making a label to describe the character
        self.character_frame = tk.Frame(self.mainframe, width=400, bd=3)
        self.character_frame.pack(fill=tk.X)

        self.character_label = tk.Label(
            self.character_frame, text="Activate Attibute", font=("Courier", 15)
        )
        self.character_label.pack()

        # trying to make a dice work, the label to print the result is in dice_roll.py
        self.dice_frame = tk.Frame(self.mainframe, width=400, bd=3)  # spirit frame
        self.dice_frame.place(relx=0.5, rely=0.5, anchor="n")
        self.label_var = tk.IntVar()
        self.display = tk.Label(
            self.dice_frame, 
            relief="ridge", 
            borderwidth=2, 
            textvariable=self.label_var
        ).pack()

        self.roll_btn = tk.Button(
            self.dice_frame,
            text="Roll 'em",
            font=("Courier", 15),
            width=15,
            command=lambda: self.roll(),
        )
        self.roll_btn.config(relief=tk.SUNKEN)
        self.roll_btn.pack()

        print(self.att_buttons)



    def feature_buttons(self, feature):
        """making buttons"""
        self.features[feature] = {}
        self.features[feature]["frame"] = tk.Frame(self.mainframe, width=400)
        self.features[feature]["frame"].pack()

        self.features[feature]["increase_button"] = tk.Button(
            self.features[feature]["frame"],
            text=f"{feature} up",
            font=("Courier", 15),
            width=15,
            command=lambda: self.character.increase_attribute(f"{feature}"),
        ).pack(side=tk.LEFT)

        self.features[feature]["decrease_button"] = tk.Button(
            self.features[feature]["frame"],
            text=f"{feature} down",
            font=("Courier", 15),
            width=15,
            command=lambda: self.character.decrease_attribute(f"{feature}"),
        ).pack(side=tk.LEFT)

        self.features[feature]["label"] = tk.Label(
            self.features[feature]["frame"],
            textvariable=self.character.attributes[f"{feature}"],
            font=("Courier", 15),
        ).pack(side=tk.RIGHT)


        self.btn_frame = tk.Frame(
            self.mainframe, height=200, width=395, bd=4, relief=tk.GROOVE
        )
        self.btn_frame.place(relx=0.5, rely=0.6, anchor="n")

        self.rules_btn = tk.Button(self.mainframe, text="RULES", font=("Courier", 15))
        self.rules_btn.place(relx=0.25, rely=0.66, anchor="n", height=120, width=170)

        self.con_btn = tk.Button(
            self.mainframe,
            text=f"RETURN TO\nDOSIER",
            font=("Courier", 15),
            justify=tk.CENTER,
            command=lambda: self.controller.show_frame("FrontPage"),
        )

        self.con_btn.place(relx=0.75, rely=0.66, anchor="n", height=120, width=170)


    def roll(self):
        """Roll dice, add modifer and print a formatted result to the UI"""
        value = random.randint(1, 6)
        if self.v_list[0].get() == 1:
            modifier = self.character.attributes["Strength"].get()
            result = int(value) + int(modifier)
            self.label_var.set(f"result: {value} + {modifier} = {result}")
        elif self.v_list[1].get() == 1:
            modifier = self.character.attributes["Smarts"].get()
            result = int(value) + int(modifier)
            self.label_var.set(f"result: {value} + {modifier} = {result}")
        elif self.v_list[2].get() == 1:
            modifier = self.character.attributes["Dexterity"].get()
            result = int(value) + int(modifier)
            self.label_var.set(f"result: {value} + {modifier} = {result}")
        elif self.v_list[3].get() == 1:
            modifier = self.character.attributes["Wisdom"].get()
            result = int(value) + int(modifier)
            self.label_var.set(f"result: {value} + {modifier} = {result}")
        elif self.v_list[4].get() == 1:
            modifier = self.character.attributes["Charisma"].get()
            result = int(value) + int(modifier)
            self.label_var.set(f"result: {value} + {modifier} = {result}")
        elif self.v_list[5].get() == 1:
            modifier = self.character.attributes["Spirit"].get()
            result = int(value) + int(modifier)
            self.label_var.set(f"result: {value} + {modifier} = {result}")

