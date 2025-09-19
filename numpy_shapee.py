'''NumPy Array Shape'''

'''Shape of an Array
The shape of an array is the number of elements in each dimension.'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.shape) #(5,)
print(arr.ndim) # 1

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr1.shape)

arr2 = np.array([[[1, 2, 3], [2, 3, 4]], [[1, 5, 7], [3, 5, 9]]])
print(arr2.shape)

'''shape = The count of rows and columns'''

'''The return value of the arr.shape is represented in a certain data type.'''

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)


'''NumPy Broadcasting '''

'''Broadcasting allows NumPy to perform operations on arrays
with different shapes by virtually expanding dimensions so 
they match the larger array's shape'''






"Weights are calculated (learned) during training — the model "
"keeps adjusting them until its predictions become accurate."