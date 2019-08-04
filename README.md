# rapid_rpg
   A small app that allows for quick rpg games among friends


## Character app spec.


The aim of this app is to allow players to create a simple RPG character and to play a simple RPG using that character's attributes from the same screen. This is made from a number of small elements of the gui: 

  1. the Character_name should be printed along the top of the display (along with the level)
	This either means theres a box where user's can type the name, or a front page that collects the data.

  2. the 5 attributes should be displayed vertically, along with +/- buttons and the current amount of "points" in each attribute
	The attributes are ['Strength', 'Dexterity', 'Wisdom', 'Charisma', 'Spirit'] and these, are modified slightly on the fly but should be remembered and reloaded each-time the app is reloaded. That means the attributes should be stored, like in a JSON or something. 

  3. a list of 5 check boxes, 1 for each attribute
	These check boxes modify the dice results by adding the number of points assigned to each attribute. 

  4. a dice rolling button (this should perform a slightly different function depending on which of the checkboxes is ticked).This is what decides the outcome of a particular event in the game. 

  5. a box that prints the result of the dice rolling app. 



This means I'll need a number of python files:

1 for tkinter (making the actually UI) 
  Within this I will need at least two pages:
  1 for the main game #This one is well underway
  1 for the character creation page
  then I need to link them some how. 
  (could maybe do with a rules page as well, but that will come in due time)

1 for the character attributes. #This one is well underway 

1 for the dice rolling and functions #Started...

   



