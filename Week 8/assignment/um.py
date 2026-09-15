import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    frequency = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    return len(frequency)

...


if __name__ == "__main__":
    main()