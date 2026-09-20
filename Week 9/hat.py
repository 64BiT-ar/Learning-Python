import random

# @classmethod - when we don't need obj, so we use it directly for class
# it is a decorator

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))

# hat = Hat()
# hat.sort("Harry")

# Class variables, exists in class itself and has only one copy and they all share that

class Hat:
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

    @classmethod
    def sort(cls, name): # pass ref to class instead of self
        print(name, "is in", random.choice(cls.houses))


Hat().sort("Harry")