#f = open("filename.txt")
#for line in f:
    #print(line, end="")
#f.close()

with open('filename.txt', 'r') as file:
    for line in file:
        print(line, end="")