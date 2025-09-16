'''Slicing arrays

Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].'''

import numpy as np

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = np.array(lst)
print(result[1:8])
print(result[1:])
print(result[:1])

''' Note: The result includes the start index, but excludes the end index.'''

# Negative Slicing

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])
print(arr[::3])


# Slicing two demisional array
nested_lst = [[1, 2, 3, 5, 9, 8], [4, 5, 6, 7, 8, 9]]

new_arr = np.array(nested_lst)
print(new_arr[1, 0:4])
print(new_arr[0:2, 1]) # From both elements, return index 1
print(new_arr[0:2, 1:4])
