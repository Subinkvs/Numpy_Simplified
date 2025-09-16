import numpy as np

nested_lst = [[1, 2, 3], [4, 5, 6], [9, 8, 10]]

arr1 = np.array(nested_lst)
arr2 = np .array(nested_lst)

print(arr1 + arr2)