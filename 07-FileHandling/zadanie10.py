f = open("student.txt","w")
dane = ["Emil", "Kulka", "UEK w Krakowie", "Informatyka Stosowana"]
for i in dane:
    f.write(i)
    f.write("\n")
f.close()


f = open("student.txt", "r")
print(f.read())