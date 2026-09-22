

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def display_main(self):
        return f"{self.name} is {self.gender} and of {self.age}y/o."

class Teacher(Person):
    def __init__(self, name, gender, age, role):
        super().__init__(name,gender,age)
        self.role = role

    def display(self):
        base_display = super().display_main()
        return f"{base_display}. Their role is {self.role}."

class Student(Person):
    def __init__(self, name, gender, age, level):
        super().__init__(name,gender,age)
        self.level = level

    def display(self):
            base_display = super().display_main()
            return f"{base_display}. They are in class {self.level}."
    
sana = Teacher("sana", "female", "28", "PT")
mohid = Student("mohid", "male", "12", "5")

print(sana.display())
print(mohid.display())