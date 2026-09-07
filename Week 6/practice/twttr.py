def main():
    inp = input("Input: ").strip()

    # omit the vowels from input
    inp = shorten(inp)

    # return the result
    print(f"Output: {inp}")


def shorten(word):
    new_str = ""
    for w in word:
        if w in ['a', 'e', 'i', 'o', 'u'] or w in ['A', 'E', 'I', 'O', 'U']:
            continue
        else:
            new_str += w

    return new_str


if __name__ == "__main__":
    main()

