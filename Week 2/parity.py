def main():
    x = int(input("What's x? "))

    # if is_even(x):
    #     print("Even")
    # else:
    #     print("Odd")

    # Might be we can simplify like

    print("Even") if is_even(x) else print("Odd")
 
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# Make is_even function more efficient by

# def is_even(n):
#     return True if n % 2 == 0 else False

# Or even more further

def is_even(n):
    return n % 2 == 0 # n % 2 == 0 itself return True or Flase based on result

main()