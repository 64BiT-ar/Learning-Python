# number 1 - Exceptions







# x = int(input("What's x? "))
# print(f"x is {x}")

# We can catch errors using try, except

# try:                                # Try doing following code
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:                  # Except ValueError, if it comes run this below
#     print("x is not an integer")

# NameError (i.e x is not defined - when int throws value error in line 8), ValueError







# ----------- Best practice is to put only code which can throw error, i.e not print statement
# try:                                # Try doing following code
#     x = int(input("What's x? "))
# except ValueError:                  # Except ValueError, if it comes run this below
#     print("x is not an integer")

# print(f"x is {x}") # Error x is not defined, because on int() it raised an error and value was never assigned to x











# -------------- Better way to do is using else block
# try:                                
#     x = int(input("What's x? "))
# except ValueError:               
#     print("x is not an integer")
# else:
#     print(f"x is {x}")              # if nothing goes wrong print x








def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt)) # Simpler way, return int(input("What's x? "))
        except ValueError:
            print("x is not an integer") # Use Pass if don't want to print anything
        else:
            return x # or break and return after loop

main()

