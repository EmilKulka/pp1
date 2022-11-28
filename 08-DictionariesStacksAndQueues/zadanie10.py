arr = [{"country":"USA", "population":331.9},
{"country":"Poland", "population":37},
{"country":"France", "population":67.5},
{"country":"Spain", "population":47},
{"country":"Germany", "population":83}
]

i = 0 
while i<len(arr):
    for k,v in arr[i].items():
        print(v,end=" ")
    print()
    i+=1
    