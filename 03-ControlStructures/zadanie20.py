try:
    n=int(input("Enter a number:"))
except:
    print("I asked for a number!")
for x in range(1,11):
    print(f'{n} x {x} = {n * x}\n')

