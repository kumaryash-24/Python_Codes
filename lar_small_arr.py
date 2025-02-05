# 1️⃣ Using a for loop (Manual Method)
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))  

min_value = arr[0]  # Assume the first element is the smallest
max_value = arr[0]  # Assume the first element is the largest

for num in arr:
    if num < min_value:
        min_value = num  # Update min_value if a smaller number is found
    if num > max_value:
        max_value = num  # Update max_value if a larger number is found

print("Smallest value:", min_value)
print("Largest value:", max_value)


# 2️⃣ Using min() and max() (Easiest Method)
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Smallest value:", min(arr))
print("Largest value:", max(arr))


# 3️⃣ Using sorted()
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

sorted_arr = sorted(arr)
print("Smallest value:", sorted_arr[0])  # First element is smallest
print("Largest value:", sorted_arr[-1])  # Last element is largest
