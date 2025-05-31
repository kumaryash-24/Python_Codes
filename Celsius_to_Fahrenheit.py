 # Celcius to fahrenheit  = (C* 9/5) + 32

celcius = int(input("Enter a temperature in Celsius: "))
far = (celcius * (9/5)) + 32
print("The converted value is", far, "Fahrenheit")       

       
# fahrenheit to celcius = 5/9 * (F - 32)
   
fahrenheit = float(input("Enter a temperature in fahrenheit: "))
celcius = 5/9 * (fahrenheit-32)
print("The converted value is", celcius, "Celcius")
