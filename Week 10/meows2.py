# argparse - docs.python.org/3/library/argparse.html
# handles all parsing automatically during CLI

import sys
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="meow n times", type=int)
args = parser.parse_args()            # automatically look for sys.argv, import sys

for _ in range(args.n):
    print("meow")