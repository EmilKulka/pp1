import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)

sum = 0

for x in temperatures:
    sum = sum + int(x)
    
avg = sum//3 

print(avg)
