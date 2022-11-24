arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = []
odd = []
for x in arr:
    if x % 2 == 0:
        even.append(x)
    elif x % 2 != 0:
        odd.append(x)

for x in even:
    print(x, end= " ")
for x in odd:
    print(x, end= " ")
        