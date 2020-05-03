'''
This is a brute force algorithm to solve the NQueens problems
Implements a visualization of the back tracking problem
Since I had the time during COVID-19!
'''
import pygame
import time

N = int(input("Enter size of board"))
speed = .1			#adjust speed to speed up or down visualization
halt = True			#stops program if a solution is found
display = True      #toggle display program, did not implement
size = N 			#renamed for readability

board = [['N' for x in range(size)] for x in range(size)]
Q_location = {}		#stores previos locations of Q so they can be removed and know where to backtrack to

def valid(i, j):

	if board[i][j] == 'Q':
		return False

	if 'Q' in board[i]:		#checks row
		return False

	for x in range(size):	#checks column
		if 'Q' == board[x][j]:
			return False
	
	for x in range(size):	#check right down diagonal
		if i + x >= size or j + x >= size:
			break
		if board[i+x][j+x] == 'Q':
			return False
	
	for x in range(size):	#check right up diagonal
		if i - x < 0 or j + x >= size:
			break
		if board[i-x][j+x] == 'Q':
			return False

	for x in range(size):	#check up left diagonal
		if i - x < 0 or j - x < 0:
			break
		if board[i-x][j-x] == 'Q':
			return False

	for x in range(size):	#check down left diagonal
		if i - x >= size or j - x < 0:
			break
		if board[i-x][j-x] == 'Q':
			return False

	return True

def remove(i, j):
	board[i][j] = 'N'

#symmetry can optimize it
def solve(square_info, gameDisplay, screen):
	i = 0
	j = 0
	total = 0
	
	while i in range(size):

		if board[i][j] == 'Q':						#backtrack if it is a Q remove it
			remove(i, j)							#remove from board
			remove_queen(screen, square_info[(i, j)]) # remove from screen
			
			if j == size-1:							
				if i == 0:							#if j is last column and i is zero then we cannot backtrack anymore thus program is done
					break
				i -= 1								#back track move up a row
				j = Q_location[i]					#grab column
				continue
			
			j +=1									#if we arent at last column, increment j as to not place Q in same spot
		
		while j in range(size):

			if not valid(i, j):						#this is just for visualizing
				set_queen(square_info[(i, j)], gameDisplay)
				remove_queen(screen, square_info[(i, j)])
			
			if valid(i, j):
				set_queen(square_info[(i, j)], gameDisplay)		#pass the coordinates for the queen
				board[i][j] = 'Q'
				Q_location[i] = j
				
				if i + 1 == size:					#all Q's have been placed 
					total += 1						#we know we reached the end of the board
					if halt:						#halts program if halt is true and there is a solution
						time.sleep(3)
					remove(i, j)					#back track and remove Q
					remove_queen(screen, square_info[(i, j)])
					display_success(screen, total)

					i -= 1
					j = Q_location[i]
					break

				j = 0								#we reset J back to zero to begin checking the next row
				i += 1								#move onto next row if Q is placed
				continue
			
			if j == size-1:			#if we reached the end of the row but cannot place, backtrack
				i -= 1				#decrement by 1 to move to pevious row
				j = Q_location[i]	#grab Q location in previous row
				break

			j += 1					#move onto next column if not valid
	
								
	print("\nTotal is: ", total)

def set_queen(square_info, gameDisplay):
	x = square_info[0][0]
	y = square_info[0][1]
	square_color = square_info[1]

	if square_color == (255, 255, 255):			#if sqaure is white put a black queen
		queen = pygame.transform.scale(pygame.image.load('black_queen.png'), (50, 50))
	else:										#if square is black put a white queen
		queen = pygame.transform.scale(pygame.image.load('white_queen.png'), (50, 50))

	gameDisplay.blit(queen, (x+2, y))
	pygame.display.update()

	time.sleep(speed)

def remove_queen(screen, square_info):
	rect = (square_info[0][0], square_info[0][1], 55, 55)
	pygame.draw.rect(screen, square_info[1], rect)
	pygame.display.update()
	time.sleep(speed)							#sleep controls how fast queens appear on screen

def display_success(screen, total):
	tan = (210, 180, 140)
	rect = (450, 720, 210, 25)
	pygame.draw.rect(screen, tan, rect)			#covers up previous font

	font = pygame.font.Font('freesansbold.ttf', 16)
	text = font.render('Total Solutions found {}'.format(total), False, (0,0,0))
	screen.blit(text, (450, 720))				#puts new text on screen
	
	pygame.display.update()

def create_board(N, screen):
	square_info = {}						#contains the coordinates of the square relative the boards i x j and the color of square
	row = -1								#row keeps track of which row we are on
											#starts at -1 since it will initally be incremented
	black = (0, 0, 0)
	white = (255, 255, 255)

	x_pos = 0
	y_pos = 50
	for x in range(N*N):

		if x % N == 0:						#makes a square by resetting the xpos and incrementing ypos
			x_pos = 200
			y_pos += 55
			row += 1							
			if N % 2 == 0:					#if N is even, it does not make a perfect checkered chess board				
				temp= white 				#to solve, everytime there is an even N 
				white = black 				#and we are at a new row, swap the values of black and white
				black = temp  

		if x % 2 == 0:						#controls switching the color value of each square w,b,w,b
			color = black
		else:
			color = white

		rect = (x_pos, y_pos, 55, 55)
		square_info[(row, x%N)] = [(x_pos, y_pos), color]	#store info about square
		pygame.draw.rect(screen, color, rect)
		x_pos += 55							#move onto the next adjacent square

	return square_info						#returns sqaure info to be used in solve method

def visual(N):
	pygame.init()

	screen = pygame.display.set_mode((640,480))
	display_width = 800
	display_height = 800

	tan = (210, 180, 140)

	gameDisplay = pygame.display.set_mode((display_width, display_height))
	gameDisplay.fill(tan)
	
	pygame.display.set_caption('N-Queens Back Tracking Visual')
	
	square_info = create_board(N, screen)
	display_success(screen, 0)
	
	crashed = False		
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
			solve(square_info, screen, gameDisplay)
			pygame.quit()
			
	pygame.quit()

visual(N)

