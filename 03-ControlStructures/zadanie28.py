fib1 = 0
fib2 = 1

for i in range(1,51):
    if i == 1:
        print(fib1 , end=" ")
    elif i == 2:
        print(fib2 , end=" ")
    else:
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        print(fib3 , end=" ")
   
    

    
    
    
     
    
    