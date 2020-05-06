n = 5												#number of verticess
show_steps = True
edges = [											#x,y,weight
		(0, 1, 2),
		(0, 3, 1),
		(0, 4, 8),
		(1, 0, 6),
		(1, 2, 3),
		(1, 3, 2),
		(2, 3, 4),
		(3, 2, 2),
		(3, 4, 3),
		(4, 0, 3),
		#each vertice has a distance of zero
		(0, 0, 0),
		(1, 1, 0),
		(2, 2, 0),
		(3, 3, 0),
		(4, 4, 0)
]

edge_list = []											#contains all new paths found
matrix = [ ["_" for x in range(n)] for x in range(n)]	#construct distance matrix
														#a number represents the weight of an edge, None is no edge
														#_ is a place holder value that will represent infinity

e_matrix = [ ["_" for x in range(n)] for x in range(n)] #matrix to show computations at each step
p_matrix = [ [0   for x in range(n)] for x in range(n)] #matrix to show shortest path

def add(operand1, operand2):
	if "_" in (operand1, operand2):						#if we are adding infinity return infinty
		return "_"
	return operand1 + operand2

def min_(operand1, operand2):
	if operand1 == "_":
		return operand2
	if operand2 == "_":
		return operand1
	return min(operand1, operand2)

def shortest_path(i, j, k):
	new_path = add(matrix[i][k], matrix[k][j])
	shortest_path = min_(matrix[i][j], new_path)			#if there is no path return the new path

	if show_steps:
		if shortest_path == new_path and new_path != matrix[i][j]:
			p_matrix[i][j] = k + 1
	edge_list.append((i, j, new_path))
	return shortest_path

def print_matrix(*args):
	e_matrix = args[0]
	if len(args) == 1:
		for row in e_matrix:
			print(row)
	else:
		p_matrix = args[1]
		print("	E 				P")
		for x in range(len(e_matrix)):
			print(" {}      	|{} ".format(e_matrix[x], p_matrix[x]))

for edge in edges:									#put edges in matrix
	i = edge[0]
	j = edge[1]
	w = edge[2]
	matrix[i][j] = w


print("----Original Matrix")						#print original matrix
print_matrix(matrix)
for k in range(n):
	for i in range(n):
		for j in range(n):
			matrix[i][j] = shortest_path(i, j, k) 		

	if show_steps:
		for edge in edge_list:
			i = edge[0]
			j = edge[1]
			w = edge[2]
			e_matrix[i][j] = w
		print("-----Step {}".format(k+1))
		print_matrix(e_matrix, p_matrix)
		edge_list = []
print("-----Final Matrix")
print_matrix(matrix)

