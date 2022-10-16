godziny=int(input('Enter Hours:\n'))
stawka=int(input('Enter Rate:\n'))
if godziny > 40:
    pay=float(godziny) * float(stawka) * 1.5
    print('Pay:',pay)
else:
    pay=float(godziny) * float(stawka)
    print('Pay',pay)




