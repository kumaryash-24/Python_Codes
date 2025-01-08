lower = int(input("Enter a lower limit here: "))
upper = int(input("Enter a upper limit here: "))

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)


# using function()

def prime_no():
    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:  # This else belongs to the for loop, not the if statement
                print(num)

lower = int(input("Enter a lower limit here: "))
upper = int(input("Enter an upper limit here: "))
prime_no()
