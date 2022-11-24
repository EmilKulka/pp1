arr = [2, 3, 2, 5, 8, 1, 9, 8]

new_arr = []

for x in arr:
    if x not in new_arr:
        new_arr.append(x)
    else:
        if x in new_arr:
            new_arr.remove(x)

print(new_arr)
    
