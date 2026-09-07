# Using backslashes and then quotation marks or else  -  \"friend\"
print('Hello, "Friend"')

# 2nd method
print("Hello, \"Friend\"")

# Another method for print function
name = input("Whats your name? ")

# Special format (f) - special paranthesis
# print(f"Hello, {name}")


# ----------- String methods --------------------


# Remove white spaces from left and right
# name = name.strip()

# Capitalize the first letter of each word
# name = name.title()

#combine into one
name = name.strip().title()

# or name = input("What's your name? ").strip().title()

# print(f"Hello, {name}")


# Splitting string into sub-strings - First and Last name

first, last = name.split(" ")

print(f"Hello, {first}")