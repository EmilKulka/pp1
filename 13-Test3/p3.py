def f1(t):
    names = []
    ages = []
    words = t.split(" ")
    for word in words:
        if word[0].isupper() == True:
            names.append(word)
        if word[0].isdigit() == True:
            while word[-1].isdigit() == False:
                word = word[:-1]
            ages.append(word)
    dic = {}
    for i in range(0,len(names)):
        dic[names[i]] = ages[i]
    newdict ={ }
    d = sorted(dic.items())
    for i in range(0,len(d)):
        newdict[d[i][0]] = d[i][1]
    return newdict

def f2(d):
    sum = 0
    for key in d:
        sum += int(d[key])
    return sum

    

print(f1("Mark is 24 and Ann is 27"))
print(f2(f1("Mark is 24 and Ann is 27")))
