"""
Matrix Multiplication Example using NumPy

Matrix multiplication is a linear algebra operation where the 
element at the (i, j) position of the result is computed by 
taking the dot product of the i-th row of the first matrix and 
the j-th column of the second matrix.

For two matrices A (m×n) and B (n×p), their product will be a 
matrix C (m×p), calculated as:

Matrix multiplication works when the number of columns of the first 
matrix equals the number of rows of the second matrix.

In this example:
    A = [[1, 2],


    
         [3, 4]]

    B = [[5, 6],
         [7, 8]]

Step-by-step calculation:

    Row 1 × Col 1 → (1×5 + 2×7) = 19
    Row 1 × Col 2 → (1×6 + 2×8) = 22
    Row 2 × Col 1 → (3×5 + 4×7) = 43
    Row 2 × Col 2 → (3×6 + 4×8) = 50

So the resulting matrix is:
c = A@B


    [[19, 22],
     [43, 50]]

No of columns of first array == No of rows of second array
     
Matrix multiplication is how the network learns and transforms data.

Matrix multiplication is used in AI to combine many input features with 
weights at once to produce outputs — this is how neural networks make predictions.

This is how a neural network layer works:
inputs × weights → outputs
"""
import numpy as np

matrix = np.array([
    [1, 2, 3],   # row 0
    [4, 5, 6]    # row 1
])

print(matrix)
print(matrix.shape) 
print(matrix.ndim)


import numpy as np
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(np.matmul(A, B))
print(A@B)
print(A.dot(B))


X = np.array([[170, 65, 20]])  # 1x3 (inputs)
W = np.array([
    [0.2, 0.4],
    [0.5, 0.1],
    [0.3, 0.7]
])  # 3x2 (weights)

output = X @ W
print(output)   # shape (1x2)