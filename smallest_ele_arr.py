# 1️⃣ Using a for loop (Manual Method)
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))  
min_value = arr[0]  # Assume the first element is the smallest

for num in arr:
    if num < min_value:
        min_value = num  # Update min_value if a smaller number is found
 
print("Smallest value:", min_value)


# 2️⃣ Using min() (Easiest Method)

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Smallest value:", min(arr))


# 3️⃣ Using sorted()
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Smallest value:", sorted(arr)[0])  # The first element in a sorted list is the smallest
