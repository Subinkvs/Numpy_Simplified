'''1D Array Slicing'''
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Q1a: Slice from index 2 to 5
print(arr[2:5])  # ?

# Q1b: Slice from index 3 to the end
print(arr[3:])   # ?

# Q1c: Slice from start to index 4 (exclusive)
print(arr[:4])   # ?

'''Negative Slicing'''

arr = np.array([5, 10, 15, 20, 25, 30, 35])

# Q2a: Get the last 3 elements
print(arr[-3:])   # ?

# Q2b: Get elements from 3rd last to 2nd last (exclusive)
print(arr[-3:-1])  # ?


'''Step Slicing'''

arr = np.array([2, 4, 6, 8, 10, 12, 14, 16])

# Q3a: Every 2nd element
print(arr[::2])    # ?

# Q3b: Every 3rd element starting from index 1
print(arr[1::3])   # ?