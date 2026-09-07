# Create a function 'convert' to turn simleys
def convert(emoticons):
    return emoticons.replace(":)", "🙂").replace(":(", "🙁")

# Implement a function main, that ask input and call convert function
def main():
    inp = input("Input: ")
    inp = convert(inp)
    print(f"Output: {inp}")

main()