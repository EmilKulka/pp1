class C():
    @staticmethod
    def m1(n):
        x = ""
        y = str(n)
        for i in y:
            if int(i) % 2 == 0:
                x += i
        return int(x)
    
    @staticmethod
    def m2(n):
        x = str(n)
        for i in range(1,len(x)-1):
            if x[i] >= x[i-1]:
                continue
            else:
                return False
        return True
    
    @staticmethod
    def m3(n):
        x = str(n)
        y = ""
        for i in range(10):
                z = str(i)
                if z not in x:
                        y += z
        return y

print(C.m1(4231564))
print(C.m1(79381))
print(C.m2(125579))
print(C.m2(4557879))
print(C.m3(23557))
print(C.m3(12340))
