import numpy as np

# Scalar arithmetic (Mathmetical operation on single value)
arr = np.array([1, 2, 3, 4, 5])

print(arr + 1)
print(arr - 1)
print(arr * 2)
print(arr / 4)
print(arr ** 3)


# Vector arithmetic ( 1D array) mathematical operations on arrays
# If you use a function that works on each element of a vector → also vector operation


array = np.array([1, 2, 3, 4, 5, 6])
array1 = np.array([1.0, 2.3, 5.1, 8.6])
print(np.sqrt(array))
print(np.round(array1))
print(np.floor(array1))
print(np.pi)






# Element wise arithmetic

array2 = np.array([1, 2, 3, 4, 5])
array3 = np.array([6, 7, 8, 9, 1])

print(array2 + array3)
print(array3 / array2)
print(array2 ** array3)

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(A * B)


# Comparison operators

scores = np.array([30, 60, 70, 87, 90, 89, 76])
print(scores == 90) # Boolean operation
print(scores > 70)
scores[ scores < 60 ] = 0
print(scores)










# Area of a circle
radii = np.array([1, 2, 3, 4])
area = np.pi * radii ** 2
print(area)







# nested_lst = [[1, 2, 3], [4, 5, 6], [9, 8, 10]]

# arr1 = np.array(nested_lst)
# arr2 = np .array(nested_lst)

# print(arr1 + arr2)