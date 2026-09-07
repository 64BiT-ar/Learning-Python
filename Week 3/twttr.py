def main():
    # Ask user the input
    inp = input("Input: ").strip()

    # omit the vowels from input
    inp = removeVowel(inp)

    # return the result
    print(f"Output: {inp}")

def removeVowel(str):
    new_str = ""
    for s in str:
        if s in ['a', 'e', 'i', 'o', 'u'] or s in ['A', 'E', 'I', 'O', 'U']:
            continue
        else:
            new_str += s

    return new_str

main()