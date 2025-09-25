# ==============================
# NumPy Aggregate + Filtering Questions
# ==============================
import numpy as np

# 1. Basic Filtering + Sum
# Given an array of marks:
marks = np.array([45, 78, 23, 90, 67, 88, 34, 59])
# → Filter only marks greater than 50
# → Find the sum of these filtered marks


# 2. Filtering + Mean
# Given an array:
arr = np.array([12, 45, 67, 89, 34, 22, 90, 100])
# → Select values between 40 and 90 (exclusive)
# → Calculate their mean

# 3. Filtering + Max
'''Create a 2D array of random integers between 10 and 100 with shape (3, 4)'''
# → Filter all values greater than 50
# → Find the maximum among the filtered values

# 4. Filtering + Min
# Given an array:
data = np.array([120, 56, 89, 45, 38, 99, 140, 110])
# → Filter all values less than 100
# → Find the minimum among the filtered values

# 5. Filter Before Sum
# Create a 2D array:
array = np.array([[10, 20, 30],
                  [40, 50, 60],
                   [70, 80, 90]])
# → Filter elements greater than 30 and less than 80
# → Compute the sum of these filtered elements

# 6. Count Filtered Elements
# Given an array of student scores:
scores = np.array([34, 56, 78, 90, 45, 66, 89, 91, 50])
# → Filter scores above 60
# → Find how many such scores there are (count)
# → Find their average

# 7. Chained Conditions + Aggregation
'''Create a random array of 15 integers between 1 and 100'''
# → Filter numbers either less than 20 OR greater than 80
# → Find their mean and sum

# 8. Aggregation on Condition
# Given a 2D array:
matrix = np.array([[23, 45, 67],
                   [89, 12, 34],
                   [56, 78, 90]])
# → Filter all even numbers
# → Calculate their maximum and minimum


# 9. Filter Outside Range
# Given an array:
arr = np.array([12, 45, 60, 75, 30, 95, 100, 20])
# → Filter all values outside the range 40–90 (<40 or >90)
# → Find the sum and count of these filtered elements

# 10. Filter with Logical NOT (~)
# Given:
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# → Filter all elements NOT greater than 40
# → Compute the mean of these remaining elements

# 11. Create a 5×5 array of random integers between 1 and 100
# → Filter elements that are multiples of 5
# → Find their sum, mean, and total count
