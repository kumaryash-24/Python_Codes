# What is a Prime Number?
# A prime number is a natural number greater than 1 that has no divisors other than 1 and itself. This means a prime number can only be divided evenly (with no remainder) by 1 and the number itself.

# Examples of Prime Numbers:
# 2, 3, 5, 7, 11, 13, 17, etc.
# Properties of Prime Numbers:
# Smallest Prime Number: The smallest prime number is 2.
# Unique Even Prime: 2 is the only even prime number. All other even numbers can be divided by 2,
# so they are not prime.
# Infinite Primes: There is an infinite number of prime numbers.
# Why is 1 Not a Prime Number?
# By definition, a prime number must have exactly two distinct positive divisors: 1 and the number itself.

# The number 1 has only one divisor (1 itself), not two.
# Including 1 as a prime number would violate the fundamental properties of primes
# used in various mathematical theorems, such as the Fundamental Theorem of Arithmetic, which states
# that every integer greater than 1 can be uniquely expressed as a product of prime numbers.


num = int(input("Enter a numbers: "))
if (num == 1):
    print("it is not a prime number")
    
if num > 1:
        for i in range(2,num): # i = 2,3,4,5,......
            if num % i == 0:
                print("it is not a prime number ")
                break
        else:
            print("it is a prime number")
            

# using function
            
def prime_no():
    if (num == 1):
        print("NOT prime")
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print("Not a prime number")
                break
        else:
            print("Prime number")
num = int(input("Enter a numbers: "))
            
prime_no()

