def occurus(number, array):
    if number in array:
        return True
    else: return False

number = 23
array = [15, 38, 7, 23, 14]
if occurus(number,array) == True:
    print(f'Number: {number}\nArray: {array}\nResult: number {number} appears int the array.')
else: print((f'Number: {number}\nArray:{array}\nResult: number {number} does not appears int the array.'))