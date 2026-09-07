# Prompts the user for an arithmetic expression
x, y, z = input("Expression: ").strip().split(" ")

x = float(x)
z = float(z)
 

# Arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place
match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "*":
        print(x*z)
    case "/":
        if(z!=0):
            print(x/z)
        else:
            print("Number can't be divided by 0")
    case _:
        print("Please select operator from +, -, *, / only.")   