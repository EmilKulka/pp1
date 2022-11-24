arr = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = 0
even = 0

for i in arr:
    while i % 2 == 0:
        even = even + 1
        break
    while i % 2 != 0:
        odd = odd + 1
        break
        
print(odd , even)
     