import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

rd = random.randint(1, level)

while True:
    guess = int(input("Guess: "))

    try:
        if guess < 1:
            continue
        else:
            if guess < rd:
                print("Too small!")
            elif guess > rd:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        print("We expected a +ve integer.")
    