films = ["Film1", "Film2", "Film3", "Film4", "FIlm5"]

f = open("films.txt", "w")
for i in films:
    f.write(i)
    f.write("\n")

f.close()

f = open("films.txt", "r")
print(f.read())