# 2 Format user name
import re

name = input("What's your name? ").strip()

matches = re.search(r"(.+), *(.+)", name)

if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = first + " " + last

print("hello,", name)

#       :=

# if matches := re.search(r"(.+), *(.+)", name): # new feature allows you to assign a value to a variable                                           and check its truth value at the same time
#     last = matches.group(1)
#     first = matches.group(2)
#     name = first + " " + last