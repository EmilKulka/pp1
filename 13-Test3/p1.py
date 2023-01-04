def f(n):
    s = ""
    for x in range(n+1):
        if x > 0:
            s = s + "/"
        if(x > 0 and x % 5 == 0):
            s = s + "-"
    if n % 5 == 0:
        s = s[:-1]
    return s
