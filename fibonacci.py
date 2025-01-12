# Fibonacci series: A sequence where each number is the sum of the two preceding ones.
# Example: 0, 1, 1, 2, 3, 5, 8, ...

# Step 1: Start with the first two numbers of the series, 0 and 1.

# Step 2: For any position 'n' (where n > 1), the number is calculated as:
#         Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)

# Step 3: Use a loop or recursion to generate the series up to the desired length.

# Step 4: Keep track of the current number and the previous number to calculate the next one.

# Step 5: Stop when the desired number of terms in the series is generated.


n = int(input("Enter a number: "))
x = 0
y = 1
z = 0
if n == 1:
    print(1)
else:
   while(z<=n):
    print(z)
    x = y
    y = z
    z = x+y


# using for loop
n = int(input("Enter a number: "))
x = 0
y = 1
z = 0
 
if n == 1:
    print(1)
else:
    for _ in range(n):
        if z > n:
            break
    print(z)  
    x = y     
    y = z     
    z = x + y 

