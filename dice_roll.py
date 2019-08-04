"""This module is for the dice rolling functions"""
from tkinter import LEFT, RIGHT, CENTER, X, Y, SUNKEN
import random
import tkinter as tk


class Die:
    """Modeling a dice"""

    def __init__(self, ivalue, parent):
        """initialise the atributes of the dice"""
        self.label_var = tk.IntVar()
        self.label_var.set(
            ivalue
        )  # this must just be the initial value of the dice before rolling
        self.display = tk.Label(
            parent, relief="ridge", borderwidth=2, textvariable=self.label_var
        )
        self.display.pack()

    def roll(self):
        """Roll dice, add modifer and print a formatted result to the UI"""
        value = random.randint(1, 6)
        result = int(value) + 1
        self.label_var.set(f"result: {value} + 1 = {result}")


""" 
------Whats left?------
    OK so, there are six check boxes in the main page which should set the modifier parameters for roll().
The player should click 2 of the check boxes which sets the modifier (the total number of points between the two selected
attributes) and then roll() should produce the result of 2d6 + the modifier and return it to the UI. 
    I think I know, or have an idea of how to do this, but it would have a lot of if statements and that seems... messy?
So I'll come back to it soon. """
