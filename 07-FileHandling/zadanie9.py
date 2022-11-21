f = open("number.txt", "r")

sum = 0 

for i in f:
    sum = sum + int(i)

f.close()
print(sum)
