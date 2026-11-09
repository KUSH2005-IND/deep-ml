def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	if not matrix:
		return []

	scale_mult=[]
	for row in matrix:
		mult_row=[]
		for val in row:
			mult_row.append(val*scalar)
		scale_mult.append(mult_row)

	return scale_mult