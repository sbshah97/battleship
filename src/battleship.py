# Welcome to the game of Battleship
# @Author: Salman Shah

# Initializing the 'Ocean'
ocean = []

# --- Game Starts here --- #
def print_ocean(ocean):
	for row in ocean:
		print " ".join(row)

# Starting the game and printing the 'Ocean'

print "Let the game of 5 x 5 Battleship begin"
#Function to print 'Ocean'
print_ocean(ocean)

# Ask user to place the ship
place_row = raw_input("Enter a valid row to place the Ship!")
place_column = raw_input("Enter a valid column to place the Ship!")

for turn in range(4):
	guess_row = randint(0,len(board-1))
	guess_column = randint(0,len(board-1))

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

	print "This was your" + turn+1 + "turn"
	print_ocean(ocean)

if turn >= 3:
	print "Game over"
	
# --- Game ends here --- #


