file  = open('countries.txt')

number = 1
for line in file:
    print(number, end=" ")
    print(line,end="")
    number += 1

file.close()