try:
    wartosc=float(input('Podaj wartość od 0.0 do 1.0:\n'))
except:
    print('Niepoprawna warotść.')
    quit()


if float(wartosc) >= 0.9:
    print('Ocena: 5,0')
elif float(wartosc) >= 0.8:
    print('Ocena: 4,5')
elif float(wartosc) >= 0.7:
    print('Ocena: 4,0')
elif float(wartosc) >= 0.6:
    print('Ocena: 3,5')
elif float(wartosc) >= 0.5:
    print('Ocena: 3,0')
elif float(wartosc) < 0.5:
    print('Ocena: 2,0')










    
