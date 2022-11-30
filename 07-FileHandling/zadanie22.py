import csv

f = open("students.txt")
reader = csv.reader(f)

list = []

for row in reader:
    list.append(row)
list.pop(0)

for i in range(0,len(list)):
        int_age = int(list[i][2])
        if int_age<=30:
            print(f"{list[i][0]} {list[i][1]} {list[i][4]} ")
