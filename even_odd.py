def even_odd():
    num = int(input("enter the numbebr: "))
     
    if num % 2 == 0:
        print("even number")
    else:
        print("Odd number")
even_odd()


# using bitwise and

num = int(input("enter the numbebr: "))
if num & 1 == 0:
    print("even")
else:
    print("odd")      
    
    
    # The condition `num & 1 == 0` is used to check if a number is even or odd using bitwise operations.
# Explanation:
# - The bitwise AND operator (`&`) compares each bit of two numbers.
# - In this case, `num & 1` isolates the least significant bit (LSB) of the binary representation of `num`.
#   - If the LSB is 0, the number is even (e.g., binary 0100 for 4).
#   - If the LSB is 1, the number is odd (e.g., binary 0101 for 5).
# - This method is efficient and directly determines the parity of the number without using modulo.
# - The condition `num & 1 == 0` evaluates to True for even numbers and False for odd numbers.

        
