# Accepts exactly one CLI argument in Pinocchio’s format
# outputs a table formatted as ASCII art using tabulate, a package on PyPI
#  Format the table using the library’s grid format

from tabulate import tabulate
import sys
import csv

if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit()

file_name = sys.argv[1]
if not file_name.endswith(".csv"):
    print("Not a Python file")
    sys.exit()

menu = []

try:
    with open(f"{file_name}", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append({"Sicilian Pizza":row["Sicilian Pizza"],
                         "Small": row["Small"],
                         "Large": row["Large"]})
except FileNotFoundError:
    print("File does not exist")
    sys.exit()

print(tabulate(menu, headers=["Sicilian Pizza","Small", "Large"]), tablefmt="grid")