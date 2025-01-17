# filter():
# Purpose: Applies a function (that returns True or False) to each element
# of an iterable and keeps only those elements for which the function returns True.
# Key Point: It filters the elements of the iterable based on the provided condition.

#using For loop

print("The Number Divisible by 13 are: ")
for i in range(1,100):
    if i % 13 == 0:
        print(i)
        
        
# Using lambda function

l = [13,25,26,78,89,39]
result = list(filter(lambda x : x%13 == 0,l))
print(result)


#user input

l = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = list(filter(lambda x: x % 13 == 0, l))
print("Numbers divisible by 13:", result)
