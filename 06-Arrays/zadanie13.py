arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

sum = 0 

for i in arr:
    for y in i:
        if y % 2 == 0:
            sum = sum + y
        
print(sum)