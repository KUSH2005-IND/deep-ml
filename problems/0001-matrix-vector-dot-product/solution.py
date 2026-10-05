def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if not a or len(a[0])!=len(b): #number of columns in a == length of b, not a means matrix is empty
		return -1
	
	result=[]

	for row in a:
		dot=0
		for i in range(len(b)):
			dot+=row[i]*b[i]
		result.append(dot)

	return result
"""
[[1,2,3],[4,5,6]] & [10,20,30]
dot = 0
dot += 1*10 → 10
dot += 2*20 → 50
dot += 3*30 → 140
result=[140]
sly for row 2
"""



	