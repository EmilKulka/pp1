f = open("zadanie16.txt", "r")
f2 = open("copy.txt", "w")

f2.write(f.read())

f.close()
f2.close()