arr = [1, 2, 3, 4, 5, 6 ,7]

i = int(input("Enter a number: "))

sum = 0 

for x in arr:
    if x > i:
        sum = sum + 1 

print(f'Number of elements greater than {i} is {sum}')