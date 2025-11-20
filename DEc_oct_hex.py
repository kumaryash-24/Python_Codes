# Decimal: The standard base-10 number system we use in everyday life, using digits 0-9.
# Binary: A base-2 number system used by computers, consisting only of 0 and 1.
# Hexadecimal: A base-16 number system, using digits 0-9 and letters A-F, often used in programming for compact representation of binary data.


decimal = int(input("Enter a number here: "))       
print("the conversion of decimal number", decimal, "is: ")         
print(bin(decimal), "in binary") # prefix is 0b  
print(oct(decimal), "in octal")  # prefix is O0          
print(hex(decimal),"in hexadecimal") # prefix is 0x      


    
