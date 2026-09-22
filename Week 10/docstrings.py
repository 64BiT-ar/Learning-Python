def meow(n: int):
    # """Meow n times."""
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of meows, one per line
    :rType: str (return type is str)
    """
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))

meow(number)
print(meow.__doc__)