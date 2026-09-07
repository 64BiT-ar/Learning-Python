name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermoine":
        print("Gryffindor")
    case "Draco":
        print("Slyntherine")
    case _:                  # Works same as else statement in if, elif, else
        print("Who? ")


# We can simplify the code like

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slyntherine")
    case _:                  # Works same as else statement in if, elif, else
        print("Who? ")