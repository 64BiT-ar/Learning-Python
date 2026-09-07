# number 3

def main():
    print_square(3)

# Prints a 3x3 square grid
# def print_square(size):
#     for i in range(size):
#         for j in range(size):
#             print("#",end="")
#         print()

# easy way
# def print_square(size):
#     for i in range(size):
#         print("#" * size)

# or

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    # print("#" * width)
    # or
    for i in range(width):
         print("#", end="")
    print()
    
main()

