# students = [
#     {"name" : "Harry", "house" : "Gryffindor"},
#     {"name" : "Hermione", "house" : "Gryffindor"},
#     {"name" : "Ron", "house" : "Gryffindor"},
#     {"name" : "Draco", "house" : "Slytherine"},
# ]

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# print(gryffindors)


# ------------------- Filter

# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key= lambda s:s["name"]):
#     print(gryffindor)


# Dict comprehension

students = ["Hermoine", "Harry", "Ron"]

gryffindors = [{"name":student, "house":"Gryffindor"} for student in students]
gryffindors = {student:"Gryffindor" for student in students}

# for student in students:
#     gryffindors.append({"name":student, "house":"Gryffindor"})

# print(gryffindors)

for index, student in enumerate(students):
    print(index, student)