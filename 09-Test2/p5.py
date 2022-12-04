def f(first_letter,last_letter):
    file = open("test.txt", "r", encoding="UTF-8")
    sum = 0
    o = file.readlines()
    for line in o:
        al = line.strip().split(" ")
        for word in al:
            if len(word) > 0:
                if (word[0]==first_letter and word[-1]==last_letter):
                    sum += 1
    return sum


print(f("w", "d"))