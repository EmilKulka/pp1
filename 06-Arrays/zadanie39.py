arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(0,len(arr)):
    row = arr[i]
    for j in range(0,len(row)):
        arr[i][j] = (j+1) * (i+1)
        print(f'{arr[i][j]}', end=" ")
    print()    
    
        
        

