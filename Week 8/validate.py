# re library, define, check for and replace patterns
# docs.python.org/3/library/re.html
# re.search(pattern, string, flags=0)

# . any char except a new line
# * 0 or more repitions
# + 1 or more repitions
# ? 0 or 1 repition
# {m} m repitions
# {m,n} m-n repitions
# ^ matches the start of string
# $ matches the end of string or new line at the end of string

import re
email = input("What's your email address? ").strip()

# raw strings print(r""hello \n world")
#validating email

if re.search(r"^.+@{1}.+\.edu$", email):
    print("Valid")
else:
    print("Invalid") 