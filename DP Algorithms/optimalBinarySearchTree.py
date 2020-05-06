from pprint import pprint

keys = [("1", .22), ("2", .18), ("3", .20), ("4", .05), ("5", .25), ("6", .02), ("7", .08)] 	#no extra key since the i aligns with the indexing
main_table = [[0 for x in range( len(keys)+1) ] for x in range( len(keys)+1) ] #size of table is one more than all the keys
root_table = [[0 for x in range( len(keys)+1) ] for x in range( len(keys)+1) ]

def init():
	i = 0
	j = 1
	while i < len(keys):
		main_table[i][j] = keys[i][1]
		root_table[i][j] = keys[i][0]
		i += 1
		j += 1

def _sum(i, j):
	total = 0
	for x in range(i, j):		#does not include j in summation since j's indexing is 1 more than the indexing of keys

		total += keys[x][1]
	return round(total, 3)

def find_min(i, j):
	probabilites = []

	for k in range(i, j):		
		prob = main_table[i][k-1+1] + main_table[k+1][j] + _sum(i, j)  #k-1+1 so that we dont go out of bounds
		
		prob = round(prob, 2)
		probabilites.append((prob, k+1))
	return min(probabilites)

def main():
	init()								#initialize table

	i = 0   							#start at first row
	j = 2								#start at column 2
	save_j = 2 							#we know the location of the last column to start the diagonal at

	while j < len(main_table):			
		result = find_min(i, j)
		main_table[i][j] = result[0]
		root_table[i][j] = result[1]

		if j == len(main_table)-1:			#if we reached the last column
				i = 0						#go back to first row
				j = save_j + 1				#set j to last place we had a j in first column
				save_j = j
		else:
			i += 1
			j += 1							#j will increment to len of main_table when save_j becomes len main_table -1
	
	pprint(main_table)
	print()
	pprint(root_table)


main()
A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
prob = .22*3 + .18*2 + .20*1 + .05*3 + .25*2 + .02*3 + .08*2

prob = round(prob, 3)
print(prob)