arr = [1, 2, 3, 4]
arr2 = [2, 1, 3, 5, 6, 4]

for x in arr:
    if x in arr2:
        continue
    elif x not in arr2:
        print(False)
        quit()
print(True)
    