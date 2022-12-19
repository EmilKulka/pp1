class Student():

    id=10000
    szkola='UEK krakow'
    def __init__(self,name,surname,kierunek):
        self.name=name
        self.surname=surname
        self.id=Student.id
        Student.id += 1
        self.kierunek=kierunek


    def __str__(self):
        return f'{self.name} {self.surname} ({self.id}), {self.kierunek}, {Student.szkola}'

s1=Student('Anna', 'MAJ', 'Applied Informatics')
print(s1)
s2=Student('aaa', 'bbb', 'Applied Informatics')
print(s2)
s3=Student('aaaa', 'bbbb', 'Applied Informatics')
print(s3)
