"""This module is about modeling the character and maybe defining the functions"""
import tkinter as tk
"""I'm gonna start with the character"""
class Character:
    """An attempt to model a charachter"""
    def __init__(self, name):
        """initialize the attributes of the character"""
        self.name = name
        self.attributes = {'Strength':1, 'Smarts': 1, 'Dexterity':1, 'Wisdom':1, 'Charisma':1, 'Spirit':1}


    def increase_attribute(self, var):
        """This is to set the attribute back to 1"""
        if self.attributes[var.title()].get() != 6:
            self.attributes[var.title()].set(self.attributes[var.title()].get() + 1)
        

    def decrease_attribute(self, var):
        """This is to set the attribute back to 1"""
        if self.attributes[var.title()].get() != 0:
            self.attributes[var.title()].set(self.attributes[var.title()].get() - 1)







