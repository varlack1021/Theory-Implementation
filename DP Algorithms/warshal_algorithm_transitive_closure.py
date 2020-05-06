n = 5												#number of verticess
show_steps = True
edges = [
		(0, 2),
		(1, 0),
		(1, 3),
		(3, 4),
		(4, 1)
]

matrix = [ [0 for x in range(n)] for x in range(n)]	#construct adjacency matrix
												#1 represents an edge where 0 is no edge
def value(i, j, k):
	bool_ =  matrix[i][j] or matrix[i][k] and matrix[k][j]
	if show_steps and bool_ and not matrix[i][j]:
		print("Step", k, "insert 1 at ", i, j)
	return bool_

for edge in edges:									#put edges in matrix
	i = edge[0]
	j = edge[1]
	matrix[i][j] = 1


for row in matrix:									#print matrix
	print(row)

for k in range(n):
	for i in range(n):
		for j in range(n):
			matrix[i][j] = value(i, j, k) 			#handles row of k

for row in matrix:									#print matrix
	print(row)


