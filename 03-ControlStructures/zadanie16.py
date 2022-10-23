try:
    n1=int(input("Enter first number:\n"))
    n2=int(input("Enter second number:\n"))
except:
    print("Enter only numbers!")
    quit()
if n1 > n2:
    print(f"Numbers in ascending order: {n2}, {n1}")
else:
    print(f"Numbers in ascending order: {n1}, {n2}")
