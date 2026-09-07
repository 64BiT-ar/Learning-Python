# ------------------ Loops

# Stupid infinity loop, ctrl + c to break it
# i = 3
# while i!=0:
#     print("Meow")

# While loop
# i = 3
# while i != 0:
#     print("Meow")
#     i = i - 1

# i = 0
# while i < 3:
#     print("paw")
#     i += 1

# For loops
# Allow us to iterate over list of items

# for i in [0,1,2]:  # i starts from 0
#     print("List")

# # Better way
# for i in range(10): # We don't use i, so we can replcae it with under-score _
#     print(i)

# for _ in range(10):
#     print(i)

# print("Meow\n" * 3, end="")

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break
#     else:
#         continue

# for _ in range(n):
#     print(_)


def main():
    num = get_number()
    meow(num)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()