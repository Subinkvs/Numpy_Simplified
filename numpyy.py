'''
What is Numpy ?

NumPy is a Python library used for working with arrays.
NumPy stands for Numerical Python.
'''
import numpy as np


arr = np.array([1, 2, 3, 4, 5])
arr = arr * 2
print(arr)


# Multiple every element of the list by 2
lst = [1, 2, 3, 4, 5]
x = [i * 2 for i in lst ]
print(x)
lst = lst * 2
print(lst)


'''Dimensions in a list
   number of square brackets you need to reach a number = the number of dimensions.
   Dimensions = the number of index levels needed to reach a single element.
'''

my_list = [[[1, 2, 3],[4, 5, 6],[7, 8, 9]] ]
print(my_list)
print(my_list[0][1][1]) # indexing


new_arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# new_arr = new_arr * 2
print(new_arr)
print(new_arr[0][0])
# Check how many dimensions the arrays have:
print(new_arr.ndim)
print(new_arr[0][0][1]+ new_arr[0][1][0])


# Multiple a nested list by 5 using numpy

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = np.array(nested_list)
result = result * 5
print(result)


nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(nested_list[0]+ nested_list[1])

new_result = np.array(nested_list)
print(new_result[0] + new_result[1])


# print([ [j* 5  for j in nested_lst[0]], [j * 5 for j in nested_lst[1] ]])

# print([[j * 5 for j in rows]for rows in nested_lst])


# Write a program to calculate the addition of nested list ?
nested_lst = [[1, 2, 3], [4, 5, 6], [9, 8, 10]]
new_lst = []
for i in range(len(nested_lst)):
    summ = 0
    for j in nested_lst:
        summ = summ + j[i]      
    new_lst.append(summ)
    

print(new_lst)

import numpy as np

result = np.array(nested_lst)
result = result * 5
print(result)

lst = [[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]
print(lst[1][0][1])

new_lst = [[1, 2, 3], [2, 4, 5]]
print(new_lst[0][2
                 ])



