# import csv

# name = input("What's your name? ")
# home = input("Where is your home? ")

# with open("students_write.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name,home])

import csv

name = input("What's your name? ")
home = input("Where is your home? ")

with open("students_write.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"]) # Specify first row, names of col
    writer.writerow({"name": name, "home": home})
    
print("Chutiya Github")