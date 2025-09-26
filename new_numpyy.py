import numpy as np

A = np.array([[1, 2, 3]])
B = np.array([[4, 5, 6]])
C = np.concatenate((A, B), axis=0) #row-wise
C = np.concatenate((A, B), axis=1) # Column-wise
print(C)