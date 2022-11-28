import json

book = {
    "nazwa": "Pan Tadeusz",
    "autor": "Adam Mickiewicz",
    "jezyk": "Polish",
    "pierwsze_wydanie":"28 czerwca 1834",
    "gatunek": "Poezja epicka",
   }

json_file = open("favourite.json", "w")
json.dump(book, json_file, indent = 4)
json_file.close()
