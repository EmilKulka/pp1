def power(x , n):
    if n == 0 and x == 0:
        return 0
    elif n == 0:
        return 1
    else: return (x * power(x, n-1))
    
   

print(power(5,3))