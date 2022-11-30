shopping_list = open("shoppinglist.txt", "w")

g_n_b = open("GrainsAndBread.txt", "r")
shopping_list.write(g_n_b.read())
g_n_b.close()
shopping_list.close()


shopping_list = open("shoppinglist.txt", "a")
shopping_list.write("\n")
shopping_list.close()

m_n_f = open("MeatAndFish.txt", "r")
shopping_list = open("shoppinglist.txt", "a")
shopping_list.write(m_n_f.read())
m_n_f.close()
shopping_list.close()

