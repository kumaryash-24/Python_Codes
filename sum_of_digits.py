# Sum of digits means if write 153 then 1+5+3 = 9 (output)

n = int(input("Enter a number: "))
sum = 0
while(n>0):
  sum = sum + n%10
  n = n//10
print("Sum of given number is: ", sum)


# for Multiply
n= int(input("Enter a number: "))
product = 1
while(n>0):
    product = product * n%10
    n = n//10
print("Product is", product)


# using for loop 
n = input("Enter a number: ") # here not int bcz n is an integer, and integers are not iterable in Python.
sum = 0
for digit in n:
    sum += int(digit)
print("Sum is", sum)









