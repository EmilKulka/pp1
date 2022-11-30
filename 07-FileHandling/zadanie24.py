txt = "To be, or not to be, that is the question"

import re

vowels = re.findall("[aeiou]",txt)

sum = 0

for x in vowels:
    sum += 1

print(sum)


