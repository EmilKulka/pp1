import json
def f(age, course, average):
    sum = 0
    f = open('test.json', "r")
    f1 = json.loads(f.read())

    for student in f1:
        if student["age"] >= age:
            courses = student["studies"]["courses"]
            for course1 in courses:
                if (course1["name"] == course):
                    dlugosc = len(course1["grades"])
                    suma = 0
                    for number in course1["grades"]:
                        suma += number
                    avg = suma / dlugosc
                    if (avg >= average):
                        sum += 1
    return sum


