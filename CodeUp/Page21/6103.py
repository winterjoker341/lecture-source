import numpy as np

np.random.seed(32)
print(np.random.random((3, 3, 3)))
A = np.random.random((10, 10))
print(np.min(A), np.max(A))
B = np.random.random(30)
print(np.mean(B))

