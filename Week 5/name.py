# Sys - number 3
# docs.python.org/3/library/sys.html

# sys.argv (argument vector) for list of all words entered during prompt

import sys

# try:
#     print("Hello, my name is", sys.argv[1], "File name:", sys.argv[0])
# except IndexError:
#     print("Too few arguments")

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("Hello, my name is", sys.argv[1])

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)

z = 2

print(f"{z:.2f}")
print(f"{z:02}")

# pypi.org - All python packages to download

