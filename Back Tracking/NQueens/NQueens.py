from pprint import pprint
import time
import sys

N = 8
size = N
board = [['N' for x in range(size)] for x in range(size)]
Q_location = {}

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

#implements back tracking here
#need to back track
#several rooms for optimization
#currently the algo checks every single possiblilty even if
#there is already a Q in the row
#also symmetry can optimize it
def solve():
	i = 0
	j = 0
	total = 0
	test = True
	while i in range(size):
		#check if this Q is at the end
		#if it is, back up a row
		#if not, just increment J

		if board[i][j] == 'Q' and j == size-1:	#backtrack checking if we are at end of row
			remove(i, j)
			if i == 0:
				break

			i -= 1
			j = Q_location[i]

		if board[i][j] == 'Q':					#
			remove(i, j)
			j +=1
		
		while j in range(size):
			if not valid(i, j):
				board[i][j] = 'Q'
				print("Removing Q at index", i, j, "------------")
				pprint(board)
				remove(i, j)
			if valid(i, j):
				print("Placing Q at", i, j)
				board[i][j] = 'Q'
				pprint(board)
				Q_location[i] = j
				if i + 1 == size:	#all Q's have been placed 
					total += 1		#we know we reached the end of the board
					print("--------{}---------".format(total))
					pprint(board)	#if we are at the last column and we placed a Q in the row

					remove(i, j)	#back track and remove Q

					i -= 1
					j = Q_location[i]
					i -= 1			#i is incrementing after this while loop so we decrement by two
					break
				j = 0			#we reset J back to zero to begin checking the next row
				i += 1			#move onto next row
				continue
			if j == size-1:			#if we reached the end of the row but cannot place, backtrack
				i -= 1
				print(i, j)
				j = Q_location[i]
				i -= 1
				break

			j += 1					#move onto next column
		i+=1					#this i moves onto the next row if the current Q was placed at the end
								
	print("\nTotal is: ", total)

board[0][7] = 'Q'
lis = [(1,2), (2, 0), (3,5), (4,1),(5,4),(6,6),(7,3)]

for position in lis:
	x = position[0]
	y = position[1]

	if valid(x, y):
		board[x][y] = 'Q'
	else:
		pprint(board)
