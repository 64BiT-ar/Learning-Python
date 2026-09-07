# students = []

# with open("student_grow.csv", "r") as file:
#     for line in file:
#         name, home = line.rstrip().split(",", maxsplit= 1)
#         student ={
#             "name" : name,
#             "home" : home
#         }
#         students.append(student)

# for student in sorted(students, key= lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

# https://docs.python.org/3/library/csv.html

# import csv

# students = []
# with open("student_grow.csv") as file:
#     reader = csv.reader(file)           # Returns a list
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key= lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

import csv

students = []
with open("student_grow.csv") as file:
    reader = csv.DictReader(file)           # Returns a dictionary, csv.DictReader recognizes that first line as column headers
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")

    
print("Chutiya Github")