# A unique number is a number that appears only once in the list. However, your code is actually storing distinct numbers (removing duplicates), not strictly unique numbers.

lst = [1,2,2,3,4,6,3,3]
uni_no= []

for num in lst:
    if num not in uni_no:
        uni_no.append(num)
print(uni_no)
