arr = [1,2,5,8,9]

max = arr[0]
n = len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i] 
         
print(max)
 
#using user input:  👇👇👇👇👇
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))  # User inputs numbers
max_value = arr[0]  # Assume the first element is the largest

for num in arr:  # Loop through each number in the list
    if num > max_value:
        max_value = num  # Update max_value if a bigger number is found

print("Maximum value:", max_value)



# using Python's built-in max() function:
arr = [1, 2, 5, 8, 9]
print(max(arr))

#using for loop only
arr = [1, 2, 5, 8, 9]
max_value = arr[0]  # Assume the first element is the largest

for num in arr:  # Loop through each number in the list
    if num > max_value:
        max_value = num  # Update max_value if a bigger number is found

print(max_value)

# Using sorted() function
arr = [1, 2, 5, 8, 9]
print(sorted(arr)[-1])  # The last element in the sorted list is the largest
