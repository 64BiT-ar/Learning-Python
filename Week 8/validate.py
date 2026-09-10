# re library, define, check for and replace patterns
# docs.python.org/3/library/re.html
# re.search(pattern, string, flags=0)

# . any char except a new line
# * 0 or more repitions
# + 1 or more repitions
# ? 0 or 1 repition (optional)
# {m} m repitions
# {m,n} m-n repitions
# ^ matches the start of string
# $ matches the end of string or new line at the end of string

import re
email = input("What's your email address? ").strip()

# raw strings print(r""hello \n world")
#validating email

# if re.search(r"^.+@{1}.+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid") 

# \d decimal digit
# \D not a decimal digit
# \s whitespace character
# \S not a whitespace character
# \w word character ... as well as numbers and underscores {a-zA-z0-9_} - {a-zA-z0-9_ } /w + whitespace 
# \W not a word character


# if re.search(r"^[a-zA-z0-9]+@\w+\.(edu|com|net|org)$", email.lower()):
#     print("Valid")
# else:
#     print("Invalid")

# flags {re.IGNORECASE, re.MULTILINE, re.DOTALL} 3rd argument in re.search

# malan@harvard.cs50.edu - multiple dots
# if re.search(r"^[a-zA-z0-9]+@(\w+\.)?\w+\.(edu|com|net|org)$", email.lower()):
#     print("Valid")
# else:
#     print("Invalid")

# or

if re.search(r"^[a-zA-z0-9]+@(\w|\.)+\.(edu|com|net|org)$", email.lower()):
    print("Valid")
else:
    print("Invalid")

# re.match match only start of string - no need of ^ at start
# re.fullmatch - match start and end of string -  no need of ^, $ sign