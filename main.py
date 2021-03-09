#!/usr/bin/env python3
"""
This program generates meme by giving image and text. It provides save option
too!
"""

import os
import sys
import argparse
from PIL import Image, ImageDraw, ImageFont


def generate_meme(image_path, meme_text):
    """
    Generate meme with image and text
    """

    pic = Image.open(image_path).convert("RGBA")

    # Resize image to fit in the meme
    pic = pic.resize((600, 300), Image.LANCZOS)

    background = Image.new("RGBA", (900, 700), "white")
    Image.Image.paste(background, pic, (150, 200))
    draw = ImageDraw.Draw(background)

    # Load font for drawing text in meme
    meme_font = ImageFont.truetype("/usr/share/fonts/ubuntu/UbuntuMono-R.ttf",
                                   50)

    draw.text((50, 50), meme_text, "black", font=meme_font)

    return background


# CLI arguments for faster usage of program
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--save", action="store_true", help="Save file")
parser.add_argument("image", type=str, help="Image path")
parser.add_argument("filename",
                    type=str,
                    default=" ",
                    help="Filename to be saved as")
args = parser.parse_args()

text = input("Enter text: ")  # Input text for meme
meme = generate_meme(args.image, text)

if args.save:
    # Save meme in current directory if file does not already exist. If it
    # exists, terminate the program otherwise it would overwrite the existing
    # file in current directory.
    if os.path.isfile(args.filename):
        print("File already exists")
        sys.exit(1)
    else:
        meme.save(args.filename)

meme.show()
