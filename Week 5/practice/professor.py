# Gen 10 diff math questions (addition) with x and y, x,y = +ve integers
# Incorrect answer display EEE
# After 3 incorrect ans, display the answer
# Prompt the user for level only form 1,2 and 3
# score, attempts

import random


def main():
    score = 0
    attempts = 0
    question_count = 0
    level = get_level()

    while question_count < 10:
        x = generate_integer(level)
        y = generate_integer(level)

        while attempts < 3:
            print(f"{question_count+1}. {x} + {y} = ", end="")
            try:
                ans = int(input(""))

                if x+y == ans:
                    attempts = 0
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = ", x+y)
            attempts = 0

        question_count += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not (level == 1 or level == 2 or level == 3):
                raise ValueError("Something went wrong.")
            return level
        except ValueError:
            continue



def generate_integer(level):
    if level == 1:
        num = random.randint(0, 9)
    elif level == 2:
        num = random.randint(10, 99)
    else:
        num = random.randint(100, 999)
    return num


if __name__ == "__main__":
    main()