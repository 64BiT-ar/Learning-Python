def main():
    yell("this", "is", "cs50")

def yell(*words):
    # uppercased = list()
    # for word in words:
    #     uppercased.append(word.upper())
    # uppercased = map(str.upper, words) # apply that function to each itr of words (word of words)

    # list comprehension
    uppercased = [word.upper() for word in words] # avoid append
    print(*uppercased)

if __name__ == "__main__":
    main()