import random
# Welcome to the game of Battleship
# @Author: Salman Shah

# Initializing the 'Ocean'
ocean_size = 5
ocean = [["_" for x in range(0,ocean_size)] for y in range(0,ocean_size)]  # declare a 2d matrix ocean

# --- Game Starts here --- #
def print_ocean(ocean):
	for row in ocean:
		print " ".join(row)

# Starting the game and printing the 'Ocean'

print "Let the game of " + str(ocean_size) + " x " + str(ocean_size) + " Battleship begin"
#Function to print 'Ocean'
print_ocean(ocean)

# Making the game interactive
computer_place_row = random.randint(0, (ocean_size-1))
computer_place_col = random.randint(0, (ocean_size-1))

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
			flag = 1 # To show where the ship is placed

board = 5 #initialize the size of the board 
count = 2 # count of the no of ships 
turn = 0

while turn <= 3:
	guess_row = random.randint(0,(ocean_size-1))
	guess_column = random.randint(0,(ocean_size-1))

	print "Computer guessed: " + str(guess_row) + " " + str(guess_column)
	if ocean[guess_row][guess_column] == "O":
		count = count - 1
		ocean[guess_row][guess_column] = "X"

	elif guess_row < 0 or guess_row > 4 and guess_column < 0 or guess_column > 4:
		print "That wasn't even in the Board!"
	elif ocean[guess_row][guess_column] == 'X':
		print "You've been at that place before"
	else:
		turn += 1
		ocean[guess_row][guess_column] = 'X'
		print "Computer you missed it."
	if count == 0:	
		print "Sorry Computer detected your ship! You LOSE!!"
		exit(0)	

	print "This was computer's " + str(turn) + " chance."
	print_ocean(ocean)

print "YAY!!! YOU WON...."