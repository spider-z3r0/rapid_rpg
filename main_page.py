
"""The aim here is to prototype the look of the main page"""
from tkinter import LEFT, RIGHT, CENTER, X, Y, RIDGE, SUNKEN, BOTH 
import tkinter as tk
from character import Character
from dice_roll import Die



class GlobalFrequency:
    """The overall class for the app"""
    def __init__(self, master):
        """intialise the attributes of the variable"""
        self.master = master
        master.title = "Global Frequency"

        
#trying to set this up with a character
        self.character = Character('spider jerselem')
        self.character.attributes['Strength'] = tk.IntVar()
        self.character.attributes['Smarts'] = tk.IntVar()
        self.character.attributes['Dexterity'] = tk.IntVar()
        self.character.attributes['Wisdom'] = tk.IntVar()
        self.character.attributes['Charisma'] = tk.IntVar()
        self.character.attributes['Spirit'] = tk.IntVar()

        self.name_label = tk.Label(master, text = self.character.name.title(), font=("Courier", 20))
        self.name_label.pack()

#This is where the buttons and stuff start, 
        self.str_frame = tk.Frame(master, width=400)#strength frame
        self.str_frame.pack(fill=X)

        self.st_btn_1 = tk.Button(self.str_frame, text = 'Strength up', font=("Courier", 15),
           width = 15, command = lambda: self.character.increase_attribute('strength'))
        self.st_btn_1.pack(side = LEFT)

        self.st_btn_2 = tk.Button(self.str_frame, text = 'Strength down', font=("Courier", 15), 
            width = 15, command = lambda: self.character.decrease_attribute('strength'))
        self.st_btn_2.pack(side = LEFT)

        self.str_label = tk.Label(self.str_frame,
                        textvariable = self.character.attributes['Strength'],
                        font=("Courier", 15))
        self.str_label.pack()


        self.sm_frame = tk.Frame(master, width=400)#Smarts frame
        self.sm_frame.pack(fill=X)

        self.sm_btn_1 = tk.Button(self.sm_frame, text = 'Smarts up', font=("Courier", 15),
           width = 15, command = lambda: self.character.increase_attribute('Smarts'))
        self.sm_btn_1.pack(side = LEFT)

        self.sm_btn_2 = tk.Button(self.sm_frame, text = 'Smarts down', font=("Courier", 15), 
            width = 15, command = lambda: self.character.decrease_attribute('Smarts'))
        self.sm_btn_2.pack(side = LEFT)

        self.sma_label = tk.Label(self.sm_frame,
                        textvariable = self.character.attributes['Smarts'],
                        font=("Courier", 15))
        self.sma_label.pack()

#Dex Buttons and stuff. 

        self.dex_frame = tk.Frame(master, width=400)#dexterity frame
        self.dex_frame.pack(fill=X)

        self.dex_btn_1 = tk.Button(self.dex_frame, text = 'Dexterity up', font=("Courier", 15),
            width = 15, command = lambda: self.character.increase_attribute('Dexterity'))
        self.dex_btn_1.pack(side = LEFT)

        self.dex_btn_2 = tk.Button(self.dex_frame, text = 'Dexterity down', font=("Courier", 15),
            width = 15, command = lambda: self.character.decrease_attribute('Dexterity'))
        self.dex_btn_2.pack(side = LEFT)

        self.dex_label = tk.Label(self.dex_frame,
            textvariable = self.character.attributes['Dexterity'],
                        font=("Courier", 15))
        self.dex_label.pack()

#Wis Buttons and stuff. 

        self.wiz_frame = tk.Frame(master, width=400)#wizdom frame
        self.wiz_frame.pack(fill=X)

        self.wiz_btn_1 = tk.Button(self.wiz_frame, text = 'Wisdom up', font=("Courier", 15),
            width = 15, command = lambda: self.character.increase_attribute('Wisdom'))
        self.wiz_btn_1.pack(side = LEFT)

        self.wiz_btn_2 = tk.Button(self.wiz_frame, text = 'Wisdom down', font=("Courier", 15),
            width = 15, command = lambda: self.character.decrease_attribute('Wisdom'))
        self.wiz_btn_2.pack(side = LEFT)

        self.wiz_label = tk.Label(self.wiz_frame,
            textvariable = self.character.attributes['Wisdom'],
                        font=("Courier", 15))
        self.wiz_label.pack()

#Char Buttons and stuff. 

        self.char_frame = tk.Frame(master, width=400)#chardom frame
        self.char_frame.pack(fill=X)

        self.char_btn_1 = tk.Button(self.char_frame, text = 'Charisma up', font=("Courier", 15),
            width = 15, command = lambda: self.character.increase_attribute('Charisma'))
        self.char_btn_1.pack(side = LEFT)

        self.char_btn_2 = tk.Button(self.char_frame, text = 'Charisma down', font=("Courier", 15),
            width = 15, command = lambda: self.character.decrease_attribute('Charisma'))
        self.char_btn_2.pack(side = LEFT)

        self.char_label = tk.Label(self.char_frame,
            textvariable = self.character.attributes['Charisma'],
                        font=("Courier", 15))
        self.char_label.pack()

#spirit Buttons and stuff. 

        self.spi_frame = tk.Frame(master, width=400)#spidom frame
        self.spi_frame.pack(fill=X)

        self.spi_btn_1 = tk.Button(self.spi_frame, text = 'Spirit up', font=("Courier", 15),
            width = 15, command = lambda: self.character.increase_attribute('Spirit'))
        self.spi_btn_1.pack(side = LEFT)

        self.spi_btn_2 = tk.Button(self.spi_frame, text = 'Spirit down', font=("Courier", 15),
            width = 15, command = lambda: self.character.decrease_attribute('Spirit'))
        self.spi_btn_2.pack(side = LEFT)

        self.spi_label = tk.Label(self.spi_frame,
            textvariable = self.character.attributes['Spirit'],
                        font=("Courier", 15))
        self.spi_label.pack()

# making a label to describe the character
        self.character_frame = tk.Frame(master, width=400, bd=3,  )
        self.character_frame.pack(fill=X)

        self.character_label= tk.Label(self.character_frame,
            text = "Activate Attibute",
            font=("Courier", 15))
        self.character_label.pack()

# setting up check button section
        self.check_frame = tk.Frame(master, width=400, bd=3, bg = 'grey')
        self.check_frame.pack()

        self.st_check = tk.Checkbutton(self.check_frame, text = 'Str', font=("Courier", 15))# strength check
        self.st_check.pack(side = LEFT)

        self.sm_check = tk.Checkbutton(self.check_frame, text = 'Sma', font=("Courier", 15))# smarts check
        self.sm_check.pack(side = LEFT)

        self.de_check = tk.Checkbutton(self.check_frame, text = 'dex', font=("Courier", 15))# dexterity check
        self.de_check.pack(side = LEFT)

        self.wi_check = tk.Checkbutton(self.check_frame, text = 'Wis', font=("Courier", 15))# wisdom check
        self.wi_check.pack(side = LEFT)

        self.ca_check = tk.Checkbutton(self.check_frame, text = 'Cha', font=("Courier", 15))# charisma check
        self.ca_check.pack(side = LEFT)

        self.sp_check = tk.Checkbutton(self.check_frame, text = 'Spi', font=("Courier", 15))# spirit check
        self.sp_check.pack(side = LEFT)

#trying to make a dice work
        self.dice_frame = tk.Frame(master, width=400, bd=3)#spidom frame
        self.dice_frame.place(relx = 0.5, rely = 0.4, anchor = 'n')
        self.dice = Die(0, self.dice_frame)
        self.roll_btn = tk.Button(self.dice_frame, text = "Roll 'em", font=("Courier", 15),
            width = 15, command = lambda: self.dice.roll(), relief = RIDGE)
        self.roll_btn.pack(fill=BOTH, expand=1)







root = tk.Tk()
root.geometry("400x600")
gui = GlobalFrequency(root)
root.mainloop()
