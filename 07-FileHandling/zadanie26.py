f = open("zadanie16.txt", "r")

r = f.read()

import re

w_6 = re.findall("\w{6}", r)

for x in w_6:
    print(x, end ="\n")