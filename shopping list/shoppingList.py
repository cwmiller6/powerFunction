#Author: Cole Miller
#Date: 22 Feb 2016

#Make an empty list of which we will add random things every time an item is added, and then code for the length of this list to compute the number for each item
numberItems = []

import os 

loop = True

while loop == True:

	#Open the shopping list OR create a new shopping list that may already have content on it and read AND write in order to write new items and read past items
	if os.path.isfile("shoppingList.txt"):
		f = open("shoppingList.txt", 'r+')
	else:
		f = open("shoppingList.txt", 'w')

	item = raw_input("Add an item to your shopping list: ")
	read = f.read()

	#If the item the user enters is in fact a real item with letters greater than or equal to 1 (not blank line) run following program
	if len(item) >= 1: 
		#append "a" every time user enters an item so that the number of items placed can be recorded using len(numberItems)
		numberItems.append("a") 
		#Write and print (read func) on the file the number of the current item using len(numberItems) with the appended "a"s, as well as the users input. Make a new line after each one so the list is organized
		f.write("{}. {}\n".format(len(numberItems), item))
		print("Your shopping list contains: \n{}".format(read))

	#If the user enters a blank item, the program will quit and the file will close
	elif len(item) < 1:
		loop = False
		f.close()




	