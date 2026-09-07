# number 1 - Libraries

# import whole library
import random

# random.choice(seq)

print(random.choice([1,4]))

# ------------

from random import choice

# no longer need of random.choice

coin = choice(["head", "tail"])

print(coin)

# random.randint(1,10) inc 1 and 10 

# randint(a,b)
number = random.randint(1,10)
print(number)

# shuffle
cards = ["jack", "queen", "king", "8"] # doesnt return any value - change original

random.shuffle(cards)
for card in cards:
    print(card)


# ------------ Statistics
# docs.python.org/3/library/statistics.html