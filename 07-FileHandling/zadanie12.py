n_p= input("Add new product")

file = open("shopping.txt", "a")

file.write(n_p)
file.write("\n")

file.close()