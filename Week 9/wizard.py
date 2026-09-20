# Inheritance

class Wizard: # Super Class
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

    ...

class Student(Wizard): # Inherited from Wizard
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    ...

class  Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print(f"{self.name} is head of {self.subject}")

    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
porfessor = Professor("Servus", "Defense against the Dark Art")

porfessor.display()
# operator overloading next