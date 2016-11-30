from __future__ import print_function
import random
from IPython.display import clear_output
# Defining a display_board
def display_board(board):
	clear_output()
	print ('   |   |')
	print (' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] )
	print ('   |   |')
	print ('------------')
	print ('   |   |')
	print (' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] )
	print ('   |   |')
	print ('------------')
	print ('   |   |')
	print (' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] )
	print ('   |   |') 

	board = ['anything', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'X']

# Taking input form the user
def player_input():
	marker = ''
	while not (marker == 'O' or marker == 'X'):
		marker = raw_input('Player 1: X or O?').upper()

		if marker == 'X':
			return ('X', 'O')
		else:
			return ('O', 'X')

# place the marker according to user's  input
def place_marker(board, marker, position):
	board[position] = marker

# check which mark has won
def win_check(board, mark):
	return (
			(board[7] == mark and board[8] == mark and board[9] == mark) or #acrosss the  top
			(board[4] == mark and board[5] == mark and board[6] == mark) or	#across the middle
			(board[1] == mark and board[2] == mark and board[3] == mark) or	#acrosss the bottom
			(board[7] == mark and board[4] == mark and board[1] == mark) or	#down left side
			(board[8] == mark and board[5] == mark and board[2] == mark) or	#down the middle
			(board[9] == mark and board[6] == mark and board[3] == mark) or	#down right side
			(board[7] == mark and board[5] == mark and board[3] == mark) or	#diagonal
			(board[9] == mark and board[5] == mark and board[1] == mark)	#diagonal
		)

# which player goes first
def choose_first():
	if random.randint(0, 1) == 0:
		return 'Player 1'
	else:
		return 'Player 2'

# Checking if the space is available on the board
def space_check(board, position):
	return board[position] == ' '
# checks if the board is full
def full_board_check(board):
	for i in range(1, 10):
		if space_check(board, i):
			return False
		return True

# player's choice for a position
def player_choice(board):
	position = ' '
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):	
		position = raw_input('Choose your next positionL (1-9) ')
	return int(position)

# to play again
def replay():
	return raw_input('Do you wanna play again? Yes or No').lower().startswith('y')

# putting it all together
print ('Welcome to Tic-Tac-Toe!')
while True:
	theBoard = [' ']*10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn + ' will go first!')

	gameOn = True

	while gameOn:
		if turn == "Player 1":
			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player1_marker, position)

			if win_check(theBoard, player1_marker):
				display_board(theBoard)
				print ('Congratulations!!, Player 1!! You won.')
				gameOn =  False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('Game draw!!!!')
					break
				else:
					turn = 'Player 2'
		else:
			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player2_marker, position)

			if win_check(theBoard, player2_marker):
				display_board(theBoard)
				print ('Congratulations!!, Player 2!! You won.')
				gameOn =  False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('Game draw!!!!')
					break
				else:
					turn = 'Player 1'
	if not replay():
		break