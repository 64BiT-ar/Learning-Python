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
    print("Not a csv file")
    sys.exit()

try:
    with open(f"{file_name}", "r") as file, open("after.csv", "w", newline='') as write:
        reader = csv.DictReader(file)
        fieldnames = ['first', 'last', "house"]
        writer = csv.DictWriter(write, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(",")
            writer.writerow(
                {
                    "first_name": first.strip(),
                    "last_name": last.strip(),
                    "house": row["house"]
                }
            )
            
except FileNotFoundError:
    print("File does not exist")
    sys.exit()