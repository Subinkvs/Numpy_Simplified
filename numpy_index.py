nested_lst = [[1, 2, 3], [4, 5, 6], [9, 8, 10]]
print(nested_lst[0][1] + nested_lst[1][0])

nested_str = [['A', 'B', 'C'], ['D', 'E', 'F']]
print(nested_str[0][0]+nested_str[1][0])


import numpy as np

result = np.array(nested_lst)
print(result[0, 0]) # First element of the first row


# Access the element on the 2nd row, 5th column:


# Accessing 3D array
new_lst = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

new_result = np.array(new_lst)
print(new_result[0, 0, 0])
print(new_result[1][0])

#Negative indexing

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])

# Write the output of the given numpy index ?
import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[1, 1, 0])



# print the number 50 from the array.?
arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = np.dot(A, B)
print(C)
