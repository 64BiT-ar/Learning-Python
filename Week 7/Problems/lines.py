# Expects one argument in CLI
# python lines.py -> Too few command-line arguments
# python lines.py hello.py goodbye.py -> Too many command-line arguments
# invalid_extension.txt -> Not a Python file
# python lines.py non_existent_file.py -> File does not exist

import sys

if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit()

file_name = sys.argv[1]
if not file_name.endswith(".py"):
    print("Not a Python file")
    sys.exit()

try:
    count_of_lines = 0

    with open(f"{file_name}", "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("#") or len(line) == 0:
                continue
            elif len(line) > 0:
                count_of_lines += 1

except FileNotFoundError:
    print("File does not exist")
    sys.exit()

# return lines of code
print(count_of_lines)