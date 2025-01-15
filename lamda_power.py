# A lambda function is a small, anonymous function in Python. 
# It is used to define simple functions in one line without using the def keyword.
# Syntax: - lambda arguments: expression

# The map() function is used to apply a function to each item in an iterable (like a list or tuple)
# and returns the results as a new iterable.
# Syntax:map(function, iterable)  in simple map function make every item iterable as here in this case

# CODE : 👇👇👇👇

nterms = int(input("Enter the number of terms: "))
result = list(map(lambda x : 2**x, range(nterms+1)))
print(result)

# if we want in the format of loop then 
for i in range(nterms + 1):
    print("The value of 2 raised to power", i, "is", result[i])  
    
    
    # if input 5 means 0,1,2,3,4,5 so output:--
    #     1,2 4,8.... it is calculating as 0 = 0, 1 = 1 , 2 = 2*2, 3 = 2*2*2, 4 = 2*2*2*2 and so on 
