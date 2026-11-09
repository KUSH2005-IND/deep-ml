import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	m=len(matrix) #no of rows
	n=len(matrix[0]) #no of columns

	means=[]
	
	if mode.lower()=="row":
		for row in matrix:
			means.append(sum(row)/n)

	elif mode.lower()=="column":
		for j in range(n):
			col_sum=0
			for i in range(m):
				col_sum+=matrix[i][j]
			means.append(col_sum/m)

#time complexity: O(mxn)
	return means
	