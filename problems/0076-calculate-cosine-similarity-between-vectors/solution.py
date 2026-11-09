import numpy as np
import math as m

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	
	# Implement your code here
	if len(v1)!=len(v2):
		return -1

	product=[]
	for i in range(len(v1)):
		product.append(v1[i]*v2[i])

	sum=0
	for j in product:
		sum=sum+j

	mag_1=np.sqrt(np.sum(v1**2))
	mag_2=np.sqrt(np.sum(v2**2))

	cosine= sum/(mag_1*mag_2)

	return cosine

			

