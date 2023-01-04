class C():
        def __init__(self,d):
                self.d = d
        
        def m(self,n):
                list = ""
                arr = []
                for student in self.d:
                        avg = sum(self.d[student])/len(self.d[student])
                        if avg >= n:
                                arr.append(student)
                arr.sort()
                for i in arr:
                        list += i
                        list += ","
                return list[:-1]


s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
print(s.m(4))
print(s.m(3))
