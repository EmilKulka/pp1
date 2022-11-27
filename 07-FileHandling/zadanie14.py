file_name = input("Enter a file name: ")

sum = 0
f = open(file_name, "r")
for line in f:
    sum = sum + 1
print(f'Number of lines: {sum}')
f.close
