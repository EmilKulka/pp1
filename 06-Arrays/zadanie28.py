def median(array):
    if int(len(array)) % 2 == 0:
        med = int((array[int(len(array)//2)]) + array[int(len(array)//2 - 1)]) / 2
        return med
    elif int(len(array)) % 2 != 0:
        med = array[int(len(array)//2)]
        return med
    
print(median([1,0,9,4,6]))
print(median([2,9]))
