# number 2

students = ["Hermoine", "Harry", "Ron"]

# for student in students:
    # print(student)

# or

# for i in range(len(students)):
#     print(i+1, students[i])


# ----------- Dictionaries

students = {
    "Hermoine" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# print(students["Hermoine"]) # Gryffindor
# print(students["Harry"]) # Gryffindor


# For loop by default print keys as in this
# for student in students:  
#     # print(student)
#     print(student, students[student], sep=", ") # return both key, value


# More on dictionaries - A list containing multiple dictionaries
students = [ 
    {"name": "Hermoine", "house":"Gryffindor", "patronus":"Otter"}, # dict-1
    {"name": "Harry", "house":"Gryffindor", "patronus":"Stag"},     # dict-2
    {"name": "Ron", "house":"Gryffindor", "patronus":"Jack Russel terrier"}, # dict-3
    {"name": "Draco", "house":"Slytherine", "patronus": None}      # dict-4
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")