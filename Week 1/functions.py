# ---------------- Functions 

# We can create our own functions using 'def' keyword

def hello():
    print("Hello, ", end="")


# name = input("What's your name? ")
# hello()
# print(name)

# 1- Functions must be defined before use or Alternate approach

# def main():
#     name = input("What's your name? ")
#     hello(name)

# def hello(name):
#     print(f"Hello, {name}")

# main()


# 2- Calculator

# we can return like n*n, n**2 (n^2) or pow(n,2)

# Creating our own square function
def square(n):
    # returning value
    return n*n 

x = int(input("What's x? "))
print(f"Square of x is: {square(x)}")