#!/usr/bin/env python3

import sys
from PIL import Image
from inky.auto import auto

inky = auto(ask_user=True, verbose=True)
saturation = 0.5

if len(sys.argv) == 1:
    print("""
Usage: {file} image-file
""".format(file=sys.argv[0]))
    sys.exit(1)

# Load the image without resizing
image = Image.open(sys.argv[1])

# Calculate the new size while maintaining the aspect ratio
width_ratio = inky.width / image.width
height_ratio = inky.height / image.height
aspect_ratio = min(width_ratio, height_ratio)

new_width = int(image.width * aspect_ratio)
new_height = int(image.height * aspect_ratio)

# Create a new image with the letterboxing
resized_image = Image.new("RGB", (inky.width, inky.height), color="white")
offset = ((inky.width - new_width) // 2, (inky.height - new_height) // 2)
resized_image.paste(image.resize((new_width, new_height)), offset)

if len(sys.argv) > 2:
    saturation = float(sys.argv[2])

inky.set_image(resized_image, saturation=saturation)
inky.show()
