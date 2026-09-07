# prompts the user for a fraction - x/y 
# +ve integers and y != 0
# output rounded to nearest integer
# 1% or less = E, 99% or more = F
# Pass "pass" in except block

def main():
    percent = get_percentage()
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

def get_percentage():
    while True:
        try:
            expression = input("Fraction: ")
            x,y = expression.split("/")
            x = int(x)
            y = int(y)

            if x < 0 or y <= 0 or x > y:
                continue

            output = round((x/y)*100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return output

main()