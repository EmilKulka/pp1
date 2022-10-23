try:
    am=int(input("Enter the amount in PLN:\n"))
except:
    print("You need to enter the amount as a number > 0")
    quit()
f=am//5
t=(am - (f * 5))//2
o=(am - (f * 5 + t *2))//1
print(f"The amount of PLN {am} in coins:\n 5 zl - {f}\n 2 zl - {t}\n 1 zl - {o}")
