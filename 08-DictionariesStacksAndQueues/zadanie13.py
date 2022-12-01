student = {
    "Name": "Emil",
    "Surname": "Kulka",
    "Age": 19,
    "Active student": True,
    "Interests":{"Sport's":"Bastketball","Computer games":"Mostly FPS games"},
    "Course": ["Programming basics","Business English B2"],
}

import json

file = open("student.json", "w")
json.dump(student, file, indent = 3)
file.close()