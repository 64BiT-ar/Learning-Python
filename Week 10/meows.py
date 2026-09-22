# MEOWS = 3 # Capitalise mean constant, don't change

# for _ in range(MEOWS):
#     print("meow")

# -------------- Class variables/constants

# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")

# cat = Cat()
# cat.meow()


# -------------------------- Type hints / mypy
# docs.python.org/3/library/typing.html

def meow(n: int):  # its a hint
    for _ in range(n):
        print("meow")
number: int = int(input("Number: "))
meow(number)