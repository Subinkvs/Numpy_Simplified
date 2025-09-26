import numpy as np

# =======================================
# 1️⃣ reshape() – Change the shape of an array
# =======================================

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(3, 2)   # 2 rows, 3 columns
print("reshape():\n", reshaped)



array = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]]])
array = array.flatten()
print(array)


new_array = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])
new_array = new_array.ravel()
print(new_array)


array = np.array([[5, 6, 7, 8]])
array = array.transpose()
print(array)

A = np.array([[1, 2, 3]])
B = np.array([[4, 5, 6]])
C = np.concatenate((A, B), axis=1)
print(C)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
vertical = np.vstack((a, b))
horizontal = np.hstack((a, b))
print(vertical)
print(horizontal)


array = np.array([[1, 3], [2, 3]])
array = np.split(array, 2)
print(array)

array = np.array([[1, 3], [2, 3], [3, 2]])
unique_arr = np.unique(array)
print(unique_arr)
