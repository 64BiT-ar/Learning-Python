class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name.")
        if house not in ["Gryffindor", "Slytherine", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid House")
        self.name = name 
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} is from {student.house}")

# def get_student():
#     student = Student() # An object of class Student
#     student.name = input("Name: ")      # can store attributes like this in class
#     student.house = input("House: ")
#     return student

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # try:
    return Student(name, house)
    # except ValueError as e:
    #     print(e)

if __name__ == "__main__":
    main()