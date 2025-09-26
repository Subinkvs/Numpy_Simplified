import numpy as np

# =======================================
# 1️⃣ reshape() – Change the shape of an array
# =======================================

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)   # 2 rows, 3 columns
print("reshape():\n", reshaped)
# Output:
# [[1 2 3]
#  [4 5 6]]

# =======================================
# 2️⃣ flatten() – Convert multi-dimensional array into 1D
# =======================================

arr2D = np.array([[1, 2, 3], [4, 5, 6]])
flat = arr2D.flatten()
print("flatten():", flat)
# Output:
# [1 2 3 4 5 6]

# =======================================
# 3️⃣ ravel() – Similar to flatten(), returns a view (faster)
# =======================================

arr2D = np.array([[10, 20], [30, 40]])
ravelled = arr2D.ravel()
print("ravel():", ravelled)
# Output:
# [10 20 30 40]

# =======================================
# 4️⃣ transpose() / .T – Swap rows and columns
# =======================================

arr2D = np.array([[1, 2, 3], [4, 5, 6]])
transposed = arr2D.transpose()  # or arr2D.T
print("transpose():\n", transposed)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# =======================================
# 5️⃣ concatenate() – Join two or more arrays
# =======================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
joined = np.concatenate((a, b))
print("concatenate():", joined)
# Output:
# [1 2 3 4 5 6]

# 2D Example
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6]])
C = np.concatenate((A, B), axis=0)
print("concatenate 2D:\n", C)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# =======================================
# 6️⃣ vstack() and hstack() – Stack vertically or horizontally
# =======================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vertical = np.vstack((a, b))
horizontal = np.hstack((a, b))

print("vstack():\n", vertical) # Row-wise
# Output:
# [[1 2 3]
#  [4 5 6]]

print("hstack():", horizontal) # Column-wise
# Output:
# [1 2 3 4 5 6]

# =======================================
# 7️⃣ split() – Split an array into multiple parts
# =======================================

arr = np.array([10, 20, 30, 40, 50, 60])
parts = np.split(arr, 3)
print("split():", parts)
# Output:
# [array([10, 20]), array([30, 40]), array([50, 60])]

# =======================================
# 8️⃣ unique() – Find unique elements in an array
# =======================================

arr = np.array([1, 2, 2, 3, 4, 4, 5])
unique_values = np.unique(arr)
print("unique():", unique_values)
# Output:
# [1 2 3 4 5]

