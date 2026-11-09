import numpy as np

def calculate_dot_product(vec1, vec2):
	if len(vec1)!=len(vec2):
		return -1

	product=[]
	for i in range(len(vec1)):
		product.append(vec1[i]*vec2[i])

	sum=0
	for j in product:
		sum=sum+j
	return sum

	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The dot product of the two vectors.
	"""
	# Your code here
	#return np.dot(vec1, vec2)
	