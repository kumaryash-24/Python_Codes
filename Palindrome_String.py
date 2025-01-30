# A palindrome is a word, number, phrase, or sequence that reads the same 
# forward and backward.

# Examples of palindromes:
# - Words: "madam", "racecar", "level"
# - Numbers: 121, 1331, 12321
# - Phrases (ignoring spaces and punctuation): "A man a plan a canal Panama"

# To check if a string or number is a palindrome:
# - Compare it with its reverse.
# - If they are the same, it is a palindrome.

# Palindromes are widely used in computer science, 
# especially in string processing and algorithm challenges.


# 👇👇👇👇👇👇👇👇👇
n =input("Enter a number: ")
rev = ''
for char in n:
    rev = char + rev
if n == rev:
    print("It is palindrome")
else:
    print("Not Palindrome")
    
    
    
# using slicing
A = input("enter a word here: ")

rev = A[::-1]

if rev == A:
    print ("the String is Palindrome")
else:
    print ('the String is not palindrome')
    
    
    
    
#  Understanding [::-1] in Python
# [::-1] is Python slicing notation used to reverse a sequence (string, list, tuple, etc.).

# Syntax of Slicing
# sequence[start:stop:step]
# start → Where to begin (default: 0).
# stop → Where to end (default: end of the sequence).
# step → Step size (default: 1).
# How [::-1] Works?
# start and stop are left empty, so it takes the entire sequence.
# step = -1, meaning it moves backward (from end to start), effectively reversing the sequence.
