f = open("zadanie20.txt" , "w")

import random

for x in range(1,51):
    f.write(f'{random.randint(100,999)}')
    f.write("\n")
    
f.close()