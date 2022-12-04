def f(array2D):
    arr = []
    for x in range(0,len(array2D[0])):
            arr.append(0)
    for x in range(0,len(array2D)):
        for y in range(0,len(array2D[x])):
            arr[y] += array2D[x][y]
    return arr
            
