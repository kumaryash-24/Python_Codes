arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

sorted_arr = sorted(set(arr))  # Remove duplicates and sort
if len(sorted_arr) < 2:
    print("No second smallest element.")
else:
    print("Second smallest element:", sorted_arr[1])


# using Function 👇👇👇👇
def find_second_smallest(arr):
    unique_sorted_arr = sorted(set(arr))  
    
    if len(unique_sorted_arr) < 2:  # Check if at least two unique numbers exist
        return "No second smallest element."
    
    return unique_sorted_arr[1]  # Second smallest element


arr = list(map(int, input("Enter numbers separated by spaces: ").split()))


print("Second smallest element:", find_second_smallest(arr))
