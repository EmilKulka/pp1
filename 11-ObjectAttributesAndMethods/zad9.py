class Arrays():
    @staticmethod
    def method_name(number_of_array_elements, value_of_array_elements):
        a=[]
        for i in range(number_of_array_elements):
            a.append(value_of_array_elements)
        return a

    @staticmethod
    def method_name2(number_of_array_elements, value_from, value_to):
        import random
        b=[]
        for j in range(number_of_array_elements):
            x=random.randrange(value_from,value_to)
            b.append(x)
        return b

    @staticmethod
    def method_name3(array, value_from, value_to):
        sum = 0 
        for i in array:
            if i >= value_from and i <= value_to:
                sum += 1
        return sum
    
m=Arrays.method_name(10,4)
m2=Arrays.method_name2(20,-7,8)
m3=Arrays.method_name3([1,2,3,4,5],-1,10)
print(m)
print(m2)
print(m3)