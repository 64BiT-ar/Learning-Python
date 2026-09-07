print("Hello, World! From hello.py")
# Comments serve as a to-do list.

# Ask user for input
name = input("What's your name? ")

"""
This is a multi-line comment
See yourself    
"""

# Print user name
# print(f"Hello,   {name}")
# print("Hello," + name)
# print("Hello, ", name, name)

# print(*objects, sep=' ', end='\n', file=None, flush=False)
# https://docs.python.org/3/library/functions.html#print

print("Hello, ", end="") # Remove the "\n" end line, by default behaviour of print func
print(name)

