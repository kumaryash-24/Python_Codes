num1 = int(input("Enter the number: "))

if num1 > 0:
    print("The number is positive")
elif num1 == 0:
    print("The number is zero")
else:
    print("The number is negative")




# using ternary operator   
num1 = int(input("Enter the number: "))
print("positive" if num1 > 0 else "negative" if num1 < 0 else "Zero")


# using function

def check_number():
    num1 = int(input("Enter the number: "))
    
    if num1 > 0:
        print("The number is positive")
    elif num1 == 0:
        print("The number is zero")  # Fixed from negative to zero
    else:
        print("The number is negative")

check_number()  # Call the function with the user input
