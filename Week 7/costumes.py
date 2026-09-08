# pillow.readthedocs.io

import sys
from PIL import Image

images = [] # to store images

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Pillow lib take care of opening closing
# Save all = save all frames
# Duration in ms
# loop = 0  infinite time

images[0].save(         # Serve as base
    "costumes.gif", 
    save_all = True, 
    append_images=[images[1]], # These are next frames
    duration=100, 
    loop=0
)