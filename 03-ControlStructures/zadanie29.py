x = int(input("Enter a number: "))

q=0
s=0
m=0

while x > 0:
    q = q + 1
    s = s + x
    m = s // q
    x = int(input("Enter a number: "))
    
    if x == 0:
        print(f' RESULT: Quantity={q}, Sum={s}, Mean={m}.')
        break
