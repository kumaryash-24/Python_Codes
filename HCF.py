 # HCF of Two Numbers
# Here, in this section we will discuss how to find HCF of two numbers in python. HCF means (Highest Common Factor)
# also known as GCD (Greatest Common Divisor).
     
# x is called HCF of a & b two conditions :

# x can completely divide both a & b leaving remainder 0
# No, other number greater than x can completely divide both a & b    
     
def findHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The HCF of the given two numbers is", findHCF(num1, num2))
