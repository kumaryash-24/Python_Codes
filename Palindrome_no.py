n = int(input("Enter a number: "))
rev = 0
x = n
while(n>0):
    rev = (rev*10 + n%10)
    n = n//10
if (x==rev):
    print("Palindrome number ")
else:
    print("Not palindrome")            
    
    
    # % gives remainder and // gives quotient by rounding off 
