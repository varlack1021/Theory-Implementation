from pprint import pprint

debug = False

items =[(0, 0), (3, 10), (8,4), (9, 9), (8, 11)] #first tuple is a place holder since i starts at 0 
												 #but I want the i's to align with the indexing of items
w = 20		

table = [[0 for x in range(w + 1)] for x in range(len(items) )]

i = 1
j = 0

while i != len(items):

	if j - items[i][0] >= 0:	#if the capacity of the item fits
		if debug:
			print(table[i-1][j], "or", (items[i][1] + table[i-1][(j-items[i][0])]), "for row ", i, "column ", j) 
		table[i][j] = max(table[i-1][j], (items[i][1] + table[i-1][(j-items[i][0])]))
	else:
		if debug:
			print(table[i-1][j], "for row", i, " column ", j, " capacity is ", items[i][0])
		table[i][j] = 	table[i-1][j]	#if not then

	if j != w:				#not at last column so we increment j
		j+=1 				
	else:					#reached last column
		j = 0				#set j to 0
		i += 1				#move onto next row





for row in table:
	print(row)