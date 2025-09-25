import numpy as np

# ===============================
# Aggregate Functions in NumPy
# ===============================
#    Aggregate functions are used to summarize data.
#    They usually take an array as input and return a single value (or summary).
#    Examples: sum, mean, max, min, argmin, argmax, etc.

# Create a 2D NumPy array (2 rows × 5 columns)
array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

# ------------------------------------
# 1. Sum of all elements in the array
# ------------------------------------
print("Sum of all elements:", np.sum(array))

# ------------------------------------
# 2. Mean (average) of all elements
# ------------------------------------
print("Mean (average):", np.mean(array))

# ------------------------------------
# 3. Maximum and Minimum values
# ------------------------------------
print("Maximum value:", np.max(array))
print("Minimum value:", np.min(array))

# ------------------------------------
# 4. Index positions of Min and Max values (in flattened array)
# ------------------------------------
print("Index of minimum value:", np.argmin(array))
print("Index of maximum value:", np.argmax(array))

# ------------------------------------
# 5. Sum across Columns (axis=0)
# ------------------------------------
# 👉 axis=0 means perform the operation vertically (column-wise)
#    It will add elements in the same column of each row.
print("Column-wise sum:", np.sum(array, axis=0))

# ------------------------------------
# 6. Sum across Rows (axis=1)
# ------------------------------------
# 👉 axis=1 means perform the operation horizontally (row-wise)
#    It will add elements in the same row.
print("Row-wise sum:", np.sum(array, axis=1))
