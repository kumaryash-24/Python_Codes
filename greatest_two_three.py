# for two numebrs:
num1 = int(input("enetr a  first number: "))
num2 = int(input("enetr a  second number: "))  # print(max(num1,num2)) we can also use max function

if(num1> num2):
    print(num1, "is greater")
elif(num1 == num2):
    print(num1,",", num2, "is equal")
elif(num1 < num2):
    print(num2, "is greater")
    
# for three numbers:
num1 = int(input("enetr a  first number: "))
num2 = int(input("enetr a  second number: "))
num3 = int(input("enetr a  third number: "))

if (num1 > num2) and (num1 > num3):
    print(num1, "is greater")
elif(num2>num3) and (num2> num1):
    print(num2,"is greater ")
elif (num1 == num2 == num3):
    print("All numbers are equal")
else:
    print(num3, "is greater")
