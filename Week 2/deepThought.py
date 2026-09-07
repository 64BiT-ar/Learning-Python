# Ask user the question yes if input is 42 else no

inp = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

match inp:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")