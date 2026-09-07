# Calculating stuff

# x = 1
# y = 2

# z = x + y


# x = int(input("What's x? "))
# y = int(input("What's y? "))

# z = int(x) + int(y)

# print(x + y) 

# ----------- Floating values (3rd Data structure)

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x/y

# https://docs.python.org/3/library/functions.html#round

# round(number[, ndigits]) - [] means it is optional
# z = round(x + y)

# round upto 2 decimal places
# z = round((x / y),2)

# print(z)

# Numeric Formating - Adding commas in big numbers
# print(f"{z:,}")

# Another method to round using f-string
print(f"{z:.2f}")


