# file i/o
# docs.python.org/3/library/functions.html#open

# name = input("What's your name? ")
# w= write, a= append, r= read
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# File automatically open and close
# with open("names.txt", "a") as file: 
#     file.write(f"{name}\n")

# rm names.txt # to remove/del file

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(f"Hello, {line.rstrip()}")

# more simpler way

# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello", line.rstrip())

# Sort the names in order and print
names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(name)

with open("names.txt") as file:
    for line in sorted(file):
        print("Hello,", line.rstrip())


print("Chutiya Github")