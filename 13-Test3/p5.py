class C():
    def __init__(self,arr):
        self.arr = arr
    
    def __str__(self):
        sum = 0
        string = ""
        for i in range(0,len(self.arr)):
            string += str(self.arr[i])
            string += "+"
            sum += self.arr[i]
        finalstring = string[:-1]
        return f'{finalstring}={sum}'
        


print(C([5, 12]))
print(C([6, 0, 15]))


