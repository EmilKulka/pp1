txt = "To be, or not to be, that is the question"

import re

sum = 0
words = re.findall("\w+",txt)

for x in words:
    sum += 1

print(sum)