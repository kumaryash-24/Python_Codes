# all positive intergers called natural numbers 

num = int(input("Enter a number: "))
sum = 0
if num <= 0:
    print("Enter a positive number.")
else:
    for i in range(1, num + 1):
        sum += i
    print("The sum of natural numbers is:", sum)


# using formulas
n = int(input("Enter a number: "))
formula = (n*(n+1)/2)
print(f"the sum of {n} is:", formula)


# if we want output in thsi format then this is Enter a number: 5 The sum of 1 + 2 + 3 + 4 + 5 is 15
n = int(input("Enter a number: "))
# Generate the series 1 + 2 + ... + n as a string
numbers = ' + '.join(str(i) for i in range(1, n+1))
# Calculate the sum using the formula
sum_of_numbers = n * (n + 1) // 2
# Print the result in the desired format
print(f"The sum of {numbers} is {sum_of_numbers}")
