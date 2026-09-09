import sys
import os
from PIL import Image, ImageOps

# 1. Validate number of command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

# 2. Check file extensions
valid_extensions = (".jpg", ".jpeg", ".png")
input_ext = os.path.splitext(input_file)[1].lower()
output_ext = os.path.splitext(output_file)[1].lower()

if input_ext not in valid_extensions or output_ext not in valid_extensions:
    sys.exit("Invalid input")

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

# 3. Process the image
try:
    photo = Image.open(input_file)
    shirt = Image.open("shirt.png")

    # Resize and crop the input photo to match shirt.png's exact size
    photo = ImageOps.fit(photo, shirt.size)

    # Paste shirt.png over photo using shirt's alpha channel as mask
    photo.paste(shirt, shirt)

    # Convert to RGB before saving to prevent JPEG RGBA errors
    photo.convert("RGB").save(output_file)

except FileNotFoundError:
    sys.exit("Input does not exist")