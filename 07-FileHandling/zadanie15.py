f = open("zadanie15.txt", "r")
counter = 0
for line in f:
    print(line,end="")
    counter += 1
    if counter == 5: input()
    if counter == 10: input()
    if counter == 15: input()
    if counter == 20: input()
    if counter == 25: input()
f.close


    