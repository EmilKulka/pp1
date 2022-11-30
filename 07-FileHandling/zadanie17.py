f = open("copylines.txt", "w")
f2 = open("zadanie16.txt", "r")
for line in f2:
    f.write(line)
f.close()
f2.close()
