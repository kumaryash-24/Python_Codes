a = input("Enter a Name: ")
vowel = 0
cons = 0
for i in range(0, len(a)):
    if (a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u" or
        a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U"):
        vowel = vowel + 1
    else:
        cons = cons + 1
print("Total Vowels: ", vowel)
print("Total Consonants: ", cons)
 

# for vowel only 
a = input("Enter a Name: ")
vowel = 0
vowels_set = "aeiouAEIOU"

for char in a:
    if char in vowels_set: 
        vowel += 1

print("Total Vowels:", vowel)
