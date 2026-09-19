class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Missing name")

        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid Age")

        self._age = age

    def display(self):
        print(f"{self.name} is {self.age} years old.")


def main():
    Ahmed = Person("Ahmed", 24)
    Ahmed.display()

if __name__ == "__main__":
    main()
