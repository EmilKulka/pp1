def minimax(array):
    min = array[0]
    max = array[0]
    for x in array:
        if x > max:
            max = x
        elif x < min:
            min = x
    new_array = [min,max]
    return new_array

print(minimax([4, 2, 8, 4, 7, 9, 5]))
