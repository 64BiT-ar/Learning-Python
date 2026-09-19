# #### 1
# docs.python.org/3/tutorials/classes.html

def main():
    # student = get_student()
    student_d = get_student_dict()

    if student_d["name"] == "padma":
        student_d["house"] = "None"

    print(f"{student_d['name']} is from {student_d['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")

    return (name, house) # tuples -  they are immutable

def get_student_dict():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()