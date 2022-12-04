import json

f = open("students.json", "r")

file = open("limited.json", "w")

r = json.load(f)

x =[]

for k in range(0,len(r)):
    row = r[k]
    x.append(row)
json.dump(x,file,indent=4)


f.close()
file.close()


#kiedys to dokoncze