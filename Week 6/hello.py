def main():
    name = input("What's your name: ")
    print(hello(name))

def hello(to="world"):
    # print("Hello, ", to) # a bad practice, it must return to test it
    return f"hello, {to}"

if __name__ == "__main__":
    main()
    