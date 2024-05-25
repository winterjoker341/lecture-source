import numpy as np

A = np.zeros((10, 10))
for i in range(10):
	for j in range(10):
		if (i==0 or i==9) or (j==0 or j==9):
			A[i][j] = 1
print(A)

B = np.zeros((8, 8), dtype=np.int32)
for i in range(8):
	for j in range(8):
		if (i%2==0 and j%2==1) or (i%2==1 and j%2==0):
			B[i][j] = 1
print(B)

