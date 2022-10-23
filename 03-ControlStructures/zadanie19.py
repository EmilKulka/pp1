try:
    dh=int(input("Enter your dogs age in human years: "))
except:
    print("Enter dogs name as a number!")
    quit()
for y in range(0,3):
    dg1=float(y*10.5)
dg2=(dh-2)*4
dg=dg1+dg2
print(f"The dog's age in human years is {dg} years.")