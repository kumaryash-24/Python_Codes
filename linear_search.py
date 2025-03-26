def linear(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = list(map(int,input("Enter the elements: ").split()))
target = int(input("Enter the no that u want to search: "))
# print(linear(arr,target))
result = linear(arr,target)
if result != -1:
    print(f"item found at index {result}")
else:
    print("Not found")
