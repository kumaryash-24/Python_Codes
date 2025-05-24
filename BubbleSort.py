size = int(input("Enter a size of the list: "))
a = []   
for i in range(size):
    val = int(input("Enter a number: "))                  
    a.append(val)                  
                          
for i in range(size):     
    for j in range(0,size-i-1):
        if(a[j] > a[j+1]):   
            a[j], a[j+1] = a[j+1], a[j]
       
print("Sorted List is: ")
print(a)    


# using function
def bubble_sort(a, size):
    for i in range(size):
        for j in range(0, size - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

size = int(input("Enter the size of the list: "))
a = []
for i in range(size):
    val = int(input("Enter a number: "))
    a.append(val)


bubble_sort(a, size)
print("Sorted List is:")
print(a)
