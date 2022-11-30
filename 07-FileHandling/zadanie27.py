f = open("grades.txt", "r")

r = f.read()

import re 

numbers = re.findall("[+-]?[0-9]+\.[0-9]+", r)

sum = 0

for x in numbers:
    float_x = float(x)
    sum += float_x
    

mean = sum / int(len(numbers))

print(mean)
        