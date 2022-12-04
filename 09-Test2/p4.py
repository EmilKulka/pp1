def f(dictionary,x,y):
    sum = 0
    for i in range(0,len(dictionary)):
        for j in range(0,len(dictionary["arr" + str((i+1))])):
            number = dictionary["arr" + str((i+1))][j]
            if (number >= x and number <= y):
                sum += number
    return sum
    

print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))
