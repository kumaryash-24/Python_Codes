# Description: 
# A leap year is a year that has 366 days instead of the usual 365. This extra day is added to the month of February (29 days) 
# to synchronize the calendar year with the solar year. A leap year occurs:
# 1. If the year is divisible by 4 but not divisible by 100, or
# 2. If the year is divisible by 400 (even if it's divisible by 100).

# Basic implementation using if-else

# Logic for leap year:
# 1. If the year is divisible by 400, it's a leap year.
# 2. If the year is divisible by 4 and not divisible by 100, it's a leap year.
# 3. Otherwise, it's not a leap year.


years = int(input("Enter a year: " ))

if (years % 400 == 0) and (years % 100 == 0):
    print(years, "is  a leap year.")

elif (years % 4 == 0) and (years % 100 != 0):
    print(years, "is a leap year")
    
else:
    print(years,"is nota leap year")
    

# using function

def leap_year():
    years = int(input("enetr  a year: "))
    
    if (years % 400 == 0) and (years % 100 == 0):
        print(years, "is a leap year")
    
    elif(years % 4 == 0) and (years %100 != 0 ):
        print(years, "is a leap year")
    else:
        print(years, "not a leap year")
leap_year()

# using calender 
import calendar
year = int(input("Enter a year: "))
if calendar.isleap(year):
    print(year, "is leap year")
else:
    print(year,"not a leap year")
    
