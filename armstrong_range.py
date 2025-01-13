# An Armstrong number (also known as a narcissistic number) is a number that is 
# equal to the sum of its own digits raised to the power of the number of digits.
# For example:
# 153 is an Armstrong number because:
# 1^3 + 5^3 + 3^3 = 153 (3 is the number of digits in 153)
# Similarly, 9474 is an Armstrong number because:
# 9^4 + 4^4 + 7^4 + 4^4 = 9474 (4 is the number of digits in 9474)
# Note: All single-digit numbers (0-9) are Armstrong numbers. Example:
# 1^1 = 1 → Armstrong number
# 5^1 = 5 → Armstrong number 
# 9^1 = 9 → Armstrong number

CODE:  👇👇👇👇

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

for num in range(lower, upper + 1):
    temp = num  
    sum = 0
    order = len(str(num))
    while temp > 0:
        digit = temp % 10 # gives last digits
        sum = sum + (digit ** order)
        temp //= 10 # removes the last digit

    if (num == sum):
        print(num) 
