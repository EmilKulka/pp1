arr = [5, 1, 9, 6, 1]

max = 0 

for x in arr:
    if x > max:
        max = x

arr.remove(max)
secondmax = 0
for x in arr:
    if x > secondmax:
        secondmax = x

print(secondmax)
        

        
        
        