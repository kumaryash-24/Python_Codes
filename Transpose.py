# Transpose of a matrix means flipping it along its diagonal.
# This swaps the rows with the corresponding columns.

# Example:
# Original Matrix (2x3):
# 1  2  3
# 4  5  6

# After Transpose (3x2):
# 1  4
# 2  5
# 3  6

# It changes the shape of the matrix such that:
# - The number of rows becomes the number of columns.
# - The number of columns becomes the number of rows.

# The transpose operation is commonly used in linear algebra, 
# data manipulation, and machine learning applications.

👇👇👇👇👇
#Solution 1 Using for loop

A = [[1,2,3],
     [4,5,6]]
T = [[0,0],
     [0,0],
     [0,0]]
for i in range (len(A)):
    for j in range (len(A[0])):
        T[j][i]=A[i][j]
for i in T:
    print (i)

#Solution 2 Using List Comprehension
A = [[1,2,3],
     [4,5,6]]

T = [[A[j][i] for j in range (len(A))] for i in range (len(A[0]))]

for i in T:
    print (i)
