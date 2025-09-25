import numpy as np

# ==============================
# NumPy Slicing Questions (1–5)
# ==============================

'''np.arange → generates sequences (like range) but as a NumPy array.

reshape → reorganizes the data into a new row–column structure.'''


# 1. Given the array:
arr = np.array([10, 20, 30, 40, 50, 60])
# → Extract elements from index 2 to 4.
print(arr[2:5])   # [30 40 50]


# 2. Given the 2D array:
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
# → Slice out the subarray containing [[6, 7], [10, 11]].
print(arr[1:3, 1:3])   # [[ 6  7]
                       #  [10 11]]


# 3. From the array:
arr = np.arange(1, 21).reshape(4, 5)
# → Slice the last two rows and first three columns.
print(arr[2:4, 0:3])
# [[11 12 13]
#  [16 17 18]]


# 4. Given:
arr = np.array([[5, 10, 15],
                [20, 25, 30],
                [35, 40, 45]])
# → Extract the second column using slicing.
print(arr[:, 1])   # [10 25 40]


# 5. Create a 1D array from 0 to 29 and extract every 3rd element using slicing.
arr = np.arange(30)
print(arr[::3])   # [ 0  3  6  9 12 15 18 21 24 27]


# =====================================
# NumPy Matrix Multiplication Questions (6–10)
# =====================================

# 6. Multiply the following two matrices using NumPy:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)
# [[19 22]
#  [43 50]]


# 7. Verify the shape of the result when multiplying a (3, 2) matrix with a (2, 4) matrix.
A = np.random.randint(1, 10, (3, 2))
B = np.random.randint(1, 10, (2, 4))
C = A @ B
print(A.shape, B.shape, C.shape)  # (3, 2), (2, 4) → (3, 4)


# 8. Given:
A = np.array([[2, 0], [1, 3]])
B = np.array([[1], [4]])
# → Perform matrix multiplication (A @ B) and explain the result.
print(A @ B)
# [[ 2*1 + 0*4 ]   → [[ 2 ]
#  [ 1*1 + 3*4 ]]     [13]]


# 9. Create a (3, 3) identity matrix using NumPy and multiply it with a (3, 3) random integer matrix.
I = np.eye(3, dtype=int)
M = np.random.randint(1, 10, (3, 3))
print("Matrix M:\n", M)
print("I @ M:\n", I @ M)   # same as M
# Observation: Multiplying by identity matrix gives the same matrix.
# np.eye(n) creates an n×n identity matrix.

# dtype=int makes the elements integers.
# I⋅M=M

# 10. Write a program to generate two (3, 3) matrices with random integers and compute:
#     - A @ B (matrix multiplication)
#     - A * B (element-wise multiplication)
# → Compare the outputs.
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))
print("A:\n", A)
print("B:\n", B)
print("A @ B:\n", A @ B)
print("A * B:\n", A * B)
# Observation: @ gives true matrix multiplication, * multiplies element by element.


# ==============================
# NumPy Slicing Questions (1–5) – Set 2
# ==============================

# 1. Given the array:
arr = np.array([5, 10, 15, 20, 25, 30, 35, 40])
# → Extract elements from index 1 to 6 with a step of 2.
print(arr[1:7:2])   # [10 20 30]


# 2. Given the 2D array:
arr = np.array([[11, 12, 13, 14],
                [21, 22, 23, 24],
                [31, 32, 33, 34],
                [41, 42, 43, 44]])
# → Slice out the subarray [[22, 23], [32, 33]].
print(arr[1:3, 1:3])   # [[22 23]
                       #  [32 33]]


# 3. From the array:
arr = np.arange(1, 26).reshape(5, 5)
# → Extract the last column using slicing.
print(arr[:, -1])   # [ 5 10 15 20 25]


# 4. Given:
arr = np.array([[100, 200, 300],
                [400, 500, 600],
                [700, 800, 900]])
# → Slice out the first two rows and last two columns.
print(arr[0:2, 1:3])
# [[200 300]
#  [500 600]]


# 5. Create a 1D array of numbers from 50 to 100 (inclusive).
# → Extract every 5th element using slicing.
arr = np.arange(50, 101)
print(arr[::5])   # [50 55 60 65 70 75 80 85 90 95 100]


# =====================================
# NumPy Matrix Multiplication Questions (6–10) – Set 2
# =====================================

# 6. Multiply the following two matrices:
A = np.array([[2, 4], [6, 8]])
B = np.array([[1, 3], [5, 7]])
print(A @ B)
# [[22 34]
#  [46 74]]


# 7. Verify the shape of the result when multiplying a (4, 3) matrix with a (3, 2) matrix.
A = np.random.randint(1, 10, (4, 3))
B = np.random.randint(1, 10, (3, 2))
C = A @ B
print(A.shape, B.shape, C.shape)  # (4, 3), (3, 2) → (4, 2)


# 8. Given:
A = np.array([[3, 1], [0, 2]])
B = np.array([[4], [5]])
# → Perform matrix multiplication (A @ B) and explain the result.
print(A @ B)
# [[3*4 + 1*5]   → [[17]
#  [0*4 + 2*5]]     [10]]


# 9. Create a (4, 4) identity matrix using NumPy and multiply it with a (4, 4) random integer matrix.
I = np.eye(4, dtype=int)
M = np.random.randint(1, 10, (4, 4))
print("Matrix M:\n", M)
print("I @ M:\n", I @ M)   # same as M
# Observation: Multiplying by identity matrix gives the same matrix.


# 10. Write a program to generate two (2, 3) and (3, 2) random integer matrices.
#     - Compute A @ B (valid matrix multiplication).
#     - Try B @ A (check the result shape).
# → Compare the two outputs.
A = np.random.randint(1, 10, (2, 3))
B = np.random.randint(1, 10, (3, 2))
print("A:\n", A)
print("B:\n", B)
print("A @ B:\n", A @ B)   # shape (2, 2)
print("B @ A:\n", B @ A)   # shape (3, 3)
# Observation: A @ B and B @ A both valid but produce different shapes and results.

