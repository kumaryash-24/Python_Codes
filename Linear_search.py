def linear_search(arr, target):
    for i in range(len(arr)):  # Go through each element
        if arr[i] == target:   # If found, return index
            return i
    return -1  # Return -1 if not found

# Taking user input for array elements
arr = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

# Taking user input for the target element
target = int(input("Enter the number to search: "))

# Calling the function and printing the result
result = linear_search(arr, target)

if result != -1:  # used when want message that item not found if only want -1 then other code 
    print(f"Item found at index {result}")
else:
    print("Item not found")


# simple code 
def linear_search(arr, target):
    for i in range(len(arr)):  # Go through each element
        if arr[i] == target:   # If found, return index
            return i
    return -1  # Return -1 if not found

# Taking user input for array elements
arr = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

# Taking user input for the target element
target = int(input("Enter the number to search: "))

# Calling the function and printing the result
print(linear_search(arr, target))
