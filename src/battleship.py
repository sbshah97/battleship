import random
# Welcome to the game of Battleship
# @Author: Salman Shah

# Initializing the 'Ocean'
ocean = [["" for x in range(0,5)] for y in range(0,5)]  # declare a 2d matrix ocean

# --- Game Starts here --- #
def print_ocean(ocean):
	for row in ocean:
		print " ".join(row)

# Starting the game and printing the 'Ocean'

print "Let the game of 5 x 5 Battleship begin"
#Function to print 'Ocean'
print_ocean(ocean)

# Ask user to place the ship
place_row = int(raw_input("Enter a valid row to place the Ship!"))
place_column = int(raw_input("Enter a valid column to place the Ship!"))
ocean[place_row][place_column] = "O" # To show where the ship is placed 
board = 5 #initialize the size of the board 
for turn in range(4):
	guess_row = random.randint(0,(board-1)) #add word random
	guess_column = random.randint(0,(board-1))

	if guess_row == place_row and guess_column == place_column:
		print "Congrats! You have won the Game!"
		break
	elif guess_row < 0 or guess_row > 4 and guess_column < 0 or guess_column > 4:
		print "That wasn't even in the Board!"
	elif ocean[guess_row][guess_column] == 'X':
		print "You've been at that place before"
	else:
		ocean[guess_row][guess_column] = 'X'
		print "Sorry man you missed it."

	print "This was your" + str(turn+1) + "turn"
	print_ocean(ocean)

if turn >= 3:
	print "Game over"
	
# --- Game ends here --- #