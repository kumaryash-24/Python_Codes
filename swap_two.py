# with using third variable

x = int(input('enter a number in x: ')) # 13
y = int(input('enter a number in y: ')) #12

temp = x
x = y
y = temp

print("X: ", x)
print("Y:", y)


# using function

def swap():
    x = int(input('enter a number in x: ')) # 13
    y = int(input('enter a number in y: ')) #12
    
    temp = x
    x = y
    y = temp
    
    print("X: ", x)
    print("Y:", y)

swap()

# without using third variable

x = int(input('enter a number in x: ')) # 13
y = int(input('enter a number in y: ')) #12

x,y = y,x

print("X: ", x)
print("Y:", y)

# without using temporary variable and by using  bitwise XOR assignment Operator
a = 10
b = 5
a ^= b
b ^= a
a ^= b
print("a: ", a)
print("b: ", b)


# XOR Rule:
# Compare the corresponding bits of two numbers.
# The result is:
# 1: if the bits are different.
# 0: if the bits are the same.
# Example 1: XOR of 5 and 3
# First, write the numbers in binary:
 # say a = 5 and b = 3
# 5 = 0101
# 3 = 0011
# Now, compare the bits bit by bit:

# Bit position	Bit of 5	Bit of 3	XOR result
# 1st               0             0            0
# 2nd	            1             0            1
# 3rd	            0             1            1
# 4th 	            1             1            0
# Result in binary: 0110

# Convert 0110 back to decimal: 6

# So, 5 ^ 3 = 6.
