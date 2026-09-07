# number 4
# pypi.org - All python packages to download

import cowsay, sys
from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
    # cowsay.cow("Hello, " + sys.argv[1])

# docs.python-requests.org