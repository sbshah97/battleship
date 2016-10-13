import random
# Welcome to the game of Battleship
# @Author: Salman Shah

# Initializing the 'Ocean'
ocean = [["-" for x in range(0,5)] for y in range(0,5)]  # declare a 2d matrix ocean

# --- Game Starts here --- #
def print_ocean(ocean):
	for row in ocean:
		print " ".join(row)

# Starting the game and printing the 'Ocean'

print "Let the game of 5 x 5 Battleship begin"
#Function to print 'Ocean'
print_ocean(ocean)

# Ask user to place the ship
flag = 0;
while (flag == 0):
	place_row = int(raw_input("Enter a valid row to place the Ship of length 2!"))
	place_column = int(raw_input("Enter a valid column to place the Ship of length 2!"))
	print "1. HORIZONTAL"
	print "2.VERTICAL"
	choice = int(raw_input("Enter your choice"))
	if (choice == 1):
		if (place_column > 3):
			continue
		else :	
			ocean[place_row][place_column] = "O"
			ocean[place_row][place_column+1] = "O" # To show where the ship is placed 
			flag = 1
	elif (choice == 2):
		if (place_row > 3):
			continue
		else :	
			ocean[place_row][place_column] = "O"
			ocean[place_row+1][place_column] = "O"	
			flag = 1	

print_ocean(ocean)
board = 5 #initialize the size of the board 
count = 2 # count of the no of ships 
for turn in range(4):
	guess_row = random.randint(0,(board-1)) #add word random
	guess_column = random.randint(0,(board-1))

	if ocean[guess_row][guess_column] == "O":
		count = count - 1
		ocean[guess_row][guess_column] = "X"
		if (count == 0):
			print "Congrats! You have won the Game!"
			break
	elif ocean[guess_row][guess_column] == 'X':
		print "You've been at that place before try again"
		turn = turn -1
	else:
		ocean[guess_row][guess_column] = 'X'
		print "Sorry man you missed it."

	print "This was your" + str(turn+1) + "turn"
	print_ocean(ocean)

if turn >= 3:
	print "Game over"
	
# --- Game ends here --- #