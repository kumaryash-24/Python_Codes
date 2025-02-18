# ASCII (American Standard Code for Information Interchange) 
# is a character encoding standard that represents text 
# using numeric codes from 0 to 127.
 
# Example 1: Convert a character to its ASCII value using ord()
#char = 'A'  # The character 'A'
#ascii_value = ord(char)  # ASCII value of 'A' is 65
#print(ascii_value)  # Output: 65

# Example 2: Convert an ASCII value to its corresponding character using chr()
#ascii_value = 66  # The ASCII value 66
#char = chr(ascii_value)  # Character corresponding to 66 is 'B'
#print(char)  # Output: 'B'

# ASCII values are used to represent characters like:
# - 'A' to 'Z' (uppercase letters): ASCII values 65 to 90
# - 'a' to 'z' (lowercase letters): ASCII values 97 to 122
# - '0' to '9' (digits): ASCII values 48 to 57
# - Special characters: Examples include '@' (64) and '#' (35)


CODE 👇👇👇👇
char = (input("Enter a letter: "))
print("The ASCII value of", char, "is", ord(char))


# USING CHAR() Function

char = int(input("Enter a number: "))
print("The value of", char, "is", chr(char))
