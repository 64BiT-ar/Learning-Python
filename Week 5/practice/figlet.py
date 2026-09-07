import sys
import random
from pyfiglet import Figlet


if len(sys.argv) == 1:

    f = Figlet()
    fonts = f.getFonts()
    font = random.choice(fonts)
    f.setFont(font=font)

    inp = input("Enter: ")
    print(f.renderText(inp))

elif len(sys.argv) == 3:

    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = Figlet(font=sys.argv[2])
        inp = input("Enter: ")
        print(f.renderText(inp))
    else:
        sys.exit()
        
else:
    sys.exit()