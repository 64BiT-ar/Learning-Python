import validators

def main():
    email = input("What's your email address? ")
    if check_email(email):
        print("Valid")
    else:
        print("Invalid")


def check_email(e):
    return True if validators.email(e) else False

if __name__ == "__main__":
    main()