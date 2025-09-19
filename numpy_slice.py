'''
Slicing arrays

Slicing in Python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].
'''





import numpy as np

# ---------- 1D Array Slicing ----------
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = np.array(lst)

print("1. result[1:8] → Elements from index 1 to 7:", result[1:8])
print("2. result[1:]  → Elements from index 1 to end:", result[1:])
print("3. result[:1]  → Elements from start to index 0:", result[:1])

'''
Note: The result includes the start index, but excludes the end index.
'''

# ---------- Negative Slicing ----------
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print("4. arr[-3:-1] → From 3rd last to 2nd last element:", arr[-3:-1])
print("5. arr[::3]   → Every 3rd element:", arr[::3])


# ---------- Slicing 2D Array ----------
nested_lst = [
    [1, 2, 3, 5, 9, 8],
    [4, 5, 6, 7, 8, 9]


]

# ---------- Slicing Row && Column --------- #

new_arr = np.array(nested_lst)

print("6. new_arr[1, 0:4]     → Row 1, columns 0 to 3:", new_arr[1, 0:4])
print("7. new_arr[0:2, 1]     → Rows 0 and 1, column 1:", new_arr[0:2, 1])
print("8. new_arr[0:2, 1:4]   → Rows 0 and 1, columns 1 to 3:", new_arr[0:2, 1:4])




