import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--name")
# args = parser.parse_args()

def total(galleons, nickel, knuks):
    return  (galleons * 17 + nickel) * 29 + knuks

# coins = [100,50,25]

# coins = {
#     "galleons":100,
#     "nickel":50,
#     "knuks":25
# }
# # for dictionaries we use double *, **coins to unpack
# print(total(**coins), "knuks")

def f(*args, **kwargs):
    print("Positional: ", args)
    print("Named: ", kwargs)

f(100,50,25,name=24)