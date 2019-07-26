"""This module is for the dice rolling functions"""
from tkinter import LEFT, RIGHT, CENTER, X, Y, SUNKEN
import random
import tkinter as tk




class Die():
    """Modeling a dice"""

    def __init__(self,ivalue,parent):
        self.label_var = tk.IntVar()
        self.label_var.set(ivalue)#this must just be the initial value of the dice before rolling
        self.display = tk.Label(parent,relief='ridge', borderwidth=2, 
                       textvariable =self.label_var)
        self.display.pack()
    
    def roll(self):
        value = random.randint(1,6)
        self.label_var.set(value)
        print (f"label_var = {value}")

