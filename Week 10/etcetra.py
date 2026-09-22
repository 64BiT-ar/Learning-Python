# Set - collection of values with no duplicates

students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermoine", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherine"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

# for house in sorted(houses):
#     print(house)


# ----------------------------- GLOBAL Variable

