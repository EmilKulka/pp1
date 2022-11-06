def letters(n):
    x=input("Enter the text:\n")
    count=0
    for a in x:
        if a == n or a == n.upper():
         count=count + 1
    return count
    
