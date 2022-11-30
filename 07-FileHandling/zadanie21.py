f = open("zadanie21.txt", "w")

for x in range(1,11):
    f.write(f"{x},{x ** 2},{x ** 3}")
    f.write("\n")