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

f = open("ICAO.txt", "w")

for k,v in ICAO.items():
    f.write(k.upper())
    f.write(" ")
    f.write(v)
    f.write("\n")
    
f.close()