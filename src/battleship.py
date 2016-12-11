import random


class Battleship:
	ocean_size = 5
	ocean_user = [["_" for x in range (0, ocean_size)] for y in range(0,ocean_size)]
	ocean_cpu = [["_" for x in range (0, ocean_size)] for y in range(0,ocean_size)]
	count_cpu = 2
	count_user = 2

	def print_ocean():
		for x in range (0, ocean_size): 
			for y in range(0,ocean_size):
				print " "

	def start():
		print "Let the game of " + str(ocean_size) + "x" + str(ocean_size) + "begin"
		print "User's Ocean"
		print_ocean()
		print "CPU's Ocean"
		print_ocean()

	def cpu_ships():
		cpu_place_row = random.randint(0, (ocean_size-2))
		cpu_place_col = random.randint(0, (ocean_size-2))
		cpu_choice = random.randint(1,2)
		if (cpu_choice == 1):
			ocean_cpu[cpu_place_row][cpu_place_col] = "O"
			ocean_cpu[cpu_place_row][cpu_place_col + 1] = "O"
			flag = 1
		elif (choice == 2):
			ocean_cpu[user_place_row][user_place_col] = "O"
			ocean_cpu[user_place_row+1][user_place_col] = "O" 

	def user_ships():
		flag = 0
		while (flag == 0):	
			user_place_row = int(raw_input("Enter a number between 0-4\n->"))
			user_place_col = int(raw_input("Enter a number between 0-4\n->"))
			print "Enter the option number for the ship to be placed"
			print "1. Horizontal"
			print "2. Vertical"
			user_choice = int(raw_input("Enter your choice\n->"))
			if (user_choice == 1):
				if (user_place_col > 3):
					continue
				else:
					ocean_user[user_place_row][user_place_col] = "O"
					ocean_user[user_place_row][user_place_col + 1] = "O"
					flag = 1
			elif (user_choice == 2):
				if(user_place_row > 3):
					continue
				else:
					ocean_user[user_place_row][user_place_col] = "O"
					ocean_user[user_place_row+1][user_place_col] = "O" 
					flag = 1

	def cpu_turn():
		flag = 0
		while (flag == 0):
			cpu_move_row = random.randint(0, ocean_size-1)
			cpu_move_col = random.randint(0, ocean_size-1)

			if(ocean_user[cpu_move_row][cpu_move_col] == "O"):
				print "That was a hit"
				count_user = count_user - 1
				flag = 1
			elif(ocean_user[cpu_move_row][cpu_move_col] == "X"):
				print "You've already hit there"
			else:
				print "Hard luck! No ship there!"
				flag = 1
		ocean_user[cpu_move_row][cpu_move_col] = "X"

	def user_turn():
		flag = 0
		while (flag == 0):	
			user_move_row = int(raw_input("Enter a number between 0 and 4\n->"))
			user_move_col = int(raw_input("Enter a number between 0 and 4\n->"))

			if(ocean_cpu[user_move_row][user_move_col] == "O"):
				print "That was a hit."
				count_cpu = count_cpu - 1
				flag = 1
			elif(ocean_cpu[user_move_row][user_move_col] == "X"):
				print "You've already hit there"
			elif(user_move_row > ocean_size-1 or user_move_col > ocean_size-1):
				print "Invalid move. Can't hit there!"
			else:
				print "Hard luck! No ship there!"
				flag = 1
		ocean_cpu[user_move_row][user_move_col] = "X"

	def user_win():
		if(count_cpu == 0):
			print "User wins. Yayyyyy!"
			exit(0)

	def cpu_win():
		if(count_user == 0):
			print "CPU wins. Yayyyyyy!"
			exit(0)

def main():
	game = Battleship() 
	game.start()
	gaem.cpu_ships()
	game.user_ships()
	while true:
		game.user_turn()
		game.user_win()
		game.cpu_turn()
		game.cpu_win()

		


















