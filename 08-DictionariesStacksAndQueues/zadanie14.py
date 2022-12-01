w = input("Enter txt: ")

ICAO = {
    "a": "Alfa",
    "b": "Bravo",
    "c": "Charlie",
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliett",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "w": "Whiskey",
    "y": "Yankee",
    "z": "Zulu",
    }


for i in w:
    if i in ICAO:
        print(ICAO[i], end=" ")
    else:
        i = i.lower()
        print(ICAO[i], end=" ")