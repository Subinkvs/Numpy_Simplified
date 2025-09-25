import numpy as np

# Broadcasting is a method in NumPy that allows arrays of different shapes 
# to be used in element-wise operations without making unnecessary copies.

# Instead of manually repeating values to match shapes, NumPy automatically 
# "stretches" one of the arrays along the mismatched dimension.


# Broadcasting Rules:
# 1. Compare dimensions from right to left.
# 2. If dimensions are equal → compatible.
# 3. If one of them is 1 → can be stretched.
# 4. Otherwise → not compatible.

'''Whenever a dimension is 1, NumPy automatically repeats it along that axis to match the other array.

That’s why a column (1) stretched horizontally

And b row (1) stretched vertically


After stretching, both arrays become the same shape → element-wise operation works.'''


# ---------------- Example 1: Scalar with Array ----------------


A = np.array([1, 2, 3, 4])   # shape (4,)
B = 5                        # scalar
C = A + B

# Scalar (5) is broadcast to [5, 5, 5, 5].

print("Example 1 result:\n", C)
# Output: [6 7 8 9]


# ---------------- Example 2: Column Vector with Row Vector ----------------
a = np.array([[1], [2], [3]])    # shape (3,1)
b = np.array([10, 20, 30])       # shape (3,)
c = a + b

# b = (3,) → treated as (1,3)

print("\nExample 2 result:\n", c)
# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]


# ---------------- Example 3: Different Shapes ----------------
x = np.array([[1, 2, 3],
              [4, 5, 6]])        # shape (2,3)

y = np.array([[10],
              [20]])             # shape (2,1)

z = x + y

print("\nExample 3 result:\n", z)



# Output:
# [[11 12 13]
#  [24 25 26]]


# ---------------- Example 4: Incompatible Shapes ----------------
a = np.array([1, 2, 3])   # shape (3,)
b = np.array([1, 2])      # shape (2,)

# This will raise an error:
# ValueError: operands could not be broadcast together
# print(a + b)


# ---------------- Summary ----------------
# - Broadcasting allows flexible element-wise operations.
# - It reduces memory usage by avoiding unnecessary copies.
# - Works for scalars, vectors, and higher-dimensional arrays.
# - Commonly used in data preprocessing, feature scaling, adding bias terms, 
#   and vectorized ML computations.

# Broadcasting in NumPy is like a shortcut: it stretches arrays so 
# mathematical operations can be applied directly, making computations faster and cleaner.
