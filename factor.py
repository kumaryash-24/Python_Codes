# Factors of a number are integers that divide the number exactly without leaving a remainder.
# For example, the factors of 28 are:
# 1, 2, 4, 7, 14, 28
# Factors always include 1 and the number itself.

num = int(input("Enter a number: "))
for i in range(1,num+1):
    if num % i == 0:
        print(f"The factor of {num} wil be: {i}")
