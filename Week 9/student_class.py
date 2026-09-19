class Student:
    def __init__(self, name, house, patronus):

        if not name:
            raise ValueError("Missing Name.")
        
        self.name = name 
        self.house = house # Also calling setter method
        self.patronus = patronus

    def __str__(self):       # Where a string is expected, this can help sending class as str
        return f"{self.name} is from {self.house}"

    # Getter - get some attribute
    @property # act as a getter
    def house(self):
        return self._house

    # Setter - set some attribute
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherine", "Ravenclaw", "Hufflepuff"]:
                    raise ValueError("Invalid House")
        self._house = house

    def charm(self):
        match self.patronus:
            case "Stag":
                return "ho"
            case "Otter":
                return "ot"
            case "Jack Russel Terrier":
                return "rjt"
            case _:
                return "wand"

def main():
    student = get_student()
    student.house = "Number Four, Privet Drive" # setter getting called
    # print(f"{student.name} is from {student.house}")
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


# def get_student():
#     student = Student() # An object of class Student
#     student.name = input("Name: ")      # can store attributes like this in class
#     student.house = input("House: ")
#     return student

if __name__ == "__main__":
    main()