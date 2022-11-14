x = ["Genowefa", "Onufry", "celestyna", "Alojzy", "Pankracy"]

max = x[0]

for i in x:
    if len(i) > len(max):
        max = i

print(max)