arr = [-15, 8, -31, 47, -2, 19]

min = arr[0]
max = arr[0]

for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i
print(max)
print(min)