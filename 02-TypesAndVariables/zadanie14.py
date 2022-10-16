#####

# Celsius degrees into Kelvin and Fahrenheit #

# reading Celsius temperature from the keyboard #
Celsius=int(input('Please enter the temperature in Celsius:'))

# calculation in Kelvin
Kelvin=float(Celsius)+273

# calculation in Fahrenheit
Fahrenheit=float(Celsius)*1.8+32

# display result
print(f'Temperature in Kelvin is {Kelvin} and temperature in Fahrenheit is {Fahrenheit}')