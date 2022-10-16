####

# BMI CALCULATOR #

# Height, Weight #
H=int(input('Please enter your Height in cm:\n'))
W=int(input('Please enter your weight in kg:\n'))

# Calculation #
bmi=round(W/(H/100)**2,1)

# Result #
print(f'BMI: {bmi}')


