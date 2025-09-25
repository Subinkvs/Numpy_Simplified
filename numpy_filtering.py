import numpy as np

'''Numpy Filtering = Refers to the process of selecting elements 
from an array that match a given condition'''

# ✅ Create a 2D NumPy array
array = np.array([[50, 60, 40, 89, 90],
                  [89, 78, 56, 75, 99]])

# --------------------------------------------
# 1️⃣ Basic filtering: Select all elements greater than 40
# --------------------------------------------
# Condition: (array > 40)
# → This returns a 1D array of all elements where the condition is True.
marks = array[array > 40]
print("All marks > 40:", marks)  
# Output: [50 60 89 90 89 78 56 75 99]
# (Notice: 40 is excluded because it's not > 40)

# --------------------------------------------
# 2️⃣ Filtering with AND (&): Select elements between 40 and 90
# --------------------------------------------
# Condition: (array > 40) & (array < 90)
# → Both conditions must be True at the same time.
# → This gives all elements > 40 AND < 90 (i.e., strictly between 40 and 90)
new_marks = array[(array > 40) & (array < 90)]
print("Marks between 40 and 90:", new_marks)  
# Output: [50 60 89 89 78 56 75]

# --------------------------------------------
# 3️⃣ Filtering with OR (|): Select elements less than 50 OR greater than 90
# --------------------------------------------
# Condition: (array < 50) | (array > 90)
# → At least one condition must be True.
# → This means we want values that are either < 50 OR > 90
new_marks = array[(array < 50) | (array > 90)]
print("Marks < 50 OR > 90:", new_marks)  
# Output: [40 99]
# Explanation:
# - 40 ✅ (because < 50)
# - 99 ✅ (because > 90)
# - All others ❌ (because they are between 50 and 90)

# Logical NOT operator
updated_marks = array[~(array < 40)]
print(updated_marks)

# The symbol ~ in Python (and NumPy) is called the tilde.