# sum() function
n = [5,8,3,2,9,70]
print(sum(n))

#other and Best way 
a = []
size = int(input("Enter the number of elements you want to insert: "))
for i in range(size):
    val = int(input("Enter a number: "))
    a.append(val)

sum = 0 
for i in range(size):  
    sum = sum + a[i]

print("Sum of elements are:", sum)


#using Sum() function and best 
a = []
size = int(input("How many elements you want to insert: "))
for i in range(size):
    val = int(input("Emter a number: "))
    a.append(val)
print("Sum of elements are: ", sum(a))
