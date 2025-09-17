"""
NumPy -> Numerical Python

- NumPy is a Python library used for working with arrays efficiently.
- It makes data handling faster, simpler, and more efficient, 
- which is why it’s used in almost every data science and machine learning project.
- The main array object in NumPy is called `ndarray`.
- `np` is a common alias for the NumPy module.
- We can create a NumPy `ndarray` using the `array()` function.
- Factory functions in Python are functions that create and return objects.
"""

nums = [1, 2, 3, 4, 5]
result = [x * 2 for x in nums]
print(result)


import numpy as np

array = np.array([1, 2, 3, 4, 5])
array = array * 2  
print("Array after multiplication:", array)
print("NumPy version:", np.__version__)
print("Type of array object:", type(array))
print("Type of np module:", type(np))

# -------------------------------
# Notes:
# -------------------------------
# 1. NumPy arrays (ndarray) allow vectorized operations on elements.
# 2. Alias: In Python, an alias is an alternative name for a module or object.
# 3. Factory function: np.array() is a factory function that creates an ndarray object.
#    - This hides the internal class constructor (ndarray) and simplifies object creation.
#    - Promotes loose coupling and code flexibility.

'''
Calculate the sum of the list with itself ? -> using list and numpy
'''




'''
Calculate the square of each number of a list ?
'''


import numpy as np

arr = np.array([1, 2, 3, 4])
arr = arr * 2
print(arr)