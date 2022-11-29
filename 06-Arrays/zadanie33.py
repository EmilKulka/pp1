arr = [1,23,5, 382,1,17,4,906]

def print_line():
    print("-"*(5*len(arr)+1))

def print_number(number):
    # left pad, dopełnienie reprezentacji do N pozycji
    print(f'| {number:3}',end ="")

print_line()
for x in arr:
    print_number(x)
print("|")
print_line()