import numpy as np


A = np.array([[2],
              [4],
              [6]])

B = np.array([[1, 2, 3]])

C= A@B
print(C)
print(C.shape)


D = np.array([[1, 2, 3, 4]])
E = np.array([[5],
              [6],
              [7],
              [8]])
result = D@E
print(result)
print(result.shape) #(1,1)

F = np.array([[2, 4], 
              [1, 3], 
              [2, 5]])
G = np.array([[6], 
              [7]])

matrix_mul = np.matmul(F, G)
print(matrix_mul)
print(matrix_mul.shape) #(3, 1)



# arr = np.array([[1], [2], [3]]) # shape(3, 1)
# arr1 = np.array([[10, 20, 30]]) # shape(1, 3)
# print(arr.shape)
# print(arr.ndim)
# print(arr1.shape)
# print(arr1.ndim)

# print(arr+arr1)


array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])

array2 = np.array([[10], 
                   [20]])

print(array1.shape)
print(array2.shape)

print(array1+array2)
c= array1 + array2
print(c.shape)
print(c.ndim)

