def compare(array1 , array2):
    if len(array1) == len(array2) and array1[0:int(len(array1)-1)] == array2[0:int(len(array2)-1)]:
        return "arrays are the same"    
    else: return "arrays aren't the same"     
            
                     
print(compare(["water","book","sky"] , ["water","book","sky"]))
print(compare([True,False],[True,False,True]))
print(compare([5,3,1] ,   [5,3,1]))
print(compare([3,2,1]  , [3,2]))