import numpy as np

# 1. Add a scalar
# Given:
arr = np.array([5, 10, 15])
# → Add 3 to every element using broadcasting.

# 2. Add a row vector to a matrix
# Given:

A = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
# → Use broadcasting to add b to each row of A.

# 3. Add a column vector to a matrix
# Given:
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
c = np.array([[100],
              [200],
              [300]])
# → Add c to each column of A.

# 4. Multiply a matrix by a row vector
# Given:
A = np.array([[2, 4, 6],
              [1, 3, 5]])
b = np.array([1, 2, 3])
# → Multiply A by b elementwise using broadcasting.

# 5. Multiply a matrix by a column vector
# Given:
A = np.array([[2, 4],
              [6, 8],
              [10, 12]])
c = np.array([[1],
              [2],
              [3]])
# → Multiply A by c elementwise using broadcasting.

# 6. Mix row and column vector
# Given:
a = np.array([[1],
              [2],
              [3]])
b = np.array([10, 20, 30])
# → Add a and b using broadcasting. Predict the shape.


# 7. Subtract two arrays
# Given:
a = np.array([[1, 2, 3]])
b = np.array([[10],
              [20],
              [30]])
# → Subtract a - b using broadcasting. What is the result shape?

# 8. Scale each column differently
# Given:
A = np.array([[1, 2, 3],
              [4, 5, 6]])
scale = np.array([2, 3, 4])
# → Multiply A by scale so each column is scaled differently.

# 9. Incompatible shapes
# Given:
a = np.array([1, 2, 3])   # shape (3,)
b = np.array([1, 2])      # shape (2,)
# → Try adding a + b. What error do you expect? Why?
