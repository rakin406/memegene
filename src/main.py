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
    pic = pic.resize((600, 300), Image.LANCZOS)

    background = Image.new("RGBA", (900, 700), "white")
    Image.Image.paste(background, pic, (150, 200))
    draw = ImageDraw.Draw(background)

    meme_font = ImageFont.truetype("/usr/share/fonts/ubuntu/UbuntuMono-R.ttf",
                                   50)
    draw.text((50, 50), meme_text, "black", font=meme_font)

    return background


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--save", action="store_true", help="Save file")
parser.add_argument("image", type=str, help="Image path")
parser.add_argument("filename",
                    type=str,
                    default=" ",
                    help="Filename to be saved as")
args = parser.parse_args()

text = input("Enter text: ")
meme = generate_meme(args.image, text)

if args.save:
    if os.path.isfile(args.filename):
        print("File already exists")
        sys.exit(1)
    else:
        meme.save(args.filename)

meme.show()
