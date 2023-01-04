def f(arr):
    s = 0
    for i in arr[0]:
        s += 1
    if len(arr) == s:
        for i in range(len(arr)-1):
            for j in range(len(arr)):
                if arr[i+1][j] == arr[0][j] * (i+2):
                    continue
                else:
                    return False
        return True
    else:
        return False
        

print(f([[1,2,3],[2,4,6],[3,6,9]]))
print(f([[1,2],[2,4]]))
print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]))
print(f([[1,2],[3,6]]))
print(f([[1,2,3],[2,4,6]]))
print(f([[1,2,3],[2,5,6]]))

            
            