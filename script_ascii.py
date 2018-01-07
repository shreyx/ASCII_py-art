from __future__ import print_function
from PIL import Image, ImageDraw, ImageFont
import os
from sys import argv, exit
import numpy as np

chars = np.asarray(list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "))  # List storing chars with gray values from 255 to 0

char_imap = {}  # Dictionary to store character mapped to gray px
types = {1: 'image/jpg', 2: 'image/png', 3: 'images/gif', 4: 'file/text'}  # Output Types
mode_types = {1: 'L', 2: 'RGB'}  # Color Mode Types

NORM = 330          # Normalization Range

TT_FONT_PATH = '/usr/share/fonts/truetype/ttf-monaco/Monaco_Linux.ttf'  # Complete Path-Name of The Truetype font file


def avg_gray_value(image):
    # Get the mean gray value of an image.
    global NORM
    image = image.convert('L')
    width, height = image.size
    total_pix_val = width * height * 255
    gray_value = 0
    for x in range(0, width):
        for y in range(0, height):
            gray_value += image.getpixel((x, y))
    return int(gray_value / total_pix_val * NORM)


def avg_rgb(image):
    # Get the mean r,g,b values of an RGB image.
    global NORM
    width, height = image.size
    total_pix_val = width * height * 255
    r_val = 0
    g_val = 0
    b_val = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = image.getpixel((x, y))
            r_val += r
            g_val += g
            b_val += b

    return (int(r_val / total_pix_val * NORM), int(g_val / total_pix_val * NORM), int(b_val / total_pix_val * NORM))


def normalize():
    # To Normalize each pixel value 0-> Darkest    10000-> Lightest
    global char_imap
    temp_imap = {}
    max = 0
    min = NORM
    for val in char_imap:
        if val > max:
            max = val
        if val < min:
            min = val
    for val in char_imap:
        temp = int(((NORM - 0) * (val - min)) / (max - min) + 0)
        temp_imap.update({temp: char_imap.get(val)})
    char_imap = temp_imap


def imager(char):
    # Get an image with a char drawn on it.
    font = ImageFont.truetype(TT_FONT_PATH, 16)
    image = Image.new('RGB', (20, 20), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), char, font=font, fill=(0, 0, 0))
    image = image.convert('L')
    return image


def initialize():
    global chars, char_imap, NORM
    for x in chars:
        im = imager(x)
        greys = avg_gray_value(im)
        if greys not in char_imap:
            tmp = {greys: x}
            char_imap.update(tmp)
    normalize()
    nearest = None
    for i in range(0, NORM + 1):
        if i in char_imap:
            nearest = i
        else:
            char_imap.update({i: char_imap.get(nearest)})


def generate_output(out_type, filename, image, mode):
    global types, mode_types, char_imap
    w, h = image.size
    font = ImageFont.truetype(TT_FONT_PATH, 8)

    if out_type == 4:
        output = open('output/' + filename + '_bw_art.txt', "w")
        for x in range(0, h, 8):
            for y in range(0, w, 8):
                im = image.crop((y, x, y + 8, x + 8))
                #r, g, b = avg_rgb(im)
                output.write(char_imap.get(avg_gray_value(im)))
            output.write('\n')
        output.close()

    else:
        if mode == 2:
            output = Image.new(mode_types.get(mode), (w, h), (255, 255, 255))
        elif mode == 1:
            output = Image.new(mode_types.get(mode), (w, h), 255)

        draw = ImageDraw.Draw(output)

        for x in range(0, w, 8):
            for y in range(0, h, 8):
                im = image.crop((x, y, x + 8, y + 8))

                if mode == 2:
                    r, g, b = avg_rgb(im)
                    draw.text((x, y), char_imap.get(avg_gray_value(im)), font=font, fill=(r, g, b))
                elif mode == 1:
                    draw.text((x, y), char_imap.get(avg_gray_value(im)), font=font)

        ext = types.get(out_type).rpartition('/')[-1]
        if mode == 1:
            output.save('output/' + filename + '_BW_art.' + ext)
        else:
            output.save('output/' + filename + '_' + mode_types.get(mode) + '_art.' + ext)


def print_usage():
    # Helper -  Prints how to execute the program and use the parameters.
    print('''
    Usage:
        python script_ascii.py [image] [output_type] [mode]

    Parameters:
        [image]         The input image file name for which ASCII art output is to be generated. Supports many formats.
        [output_type]   An Integer Value.The type of output file/image.
                        1 : 'image/jpg'
                        2 : 'image/png'
                        3 : 'images/gif'
                        4 : 'file/text'

        [mode]          The Color Mode Of The Output image
                        1 : 'L' ( Black-White / GrayScale )
                        2 : 'RGB' / Colored

                        Note# : file/text supports only black-white

    Example:
        python script_ascii.py images/wall.jpg 1 1
         - This loads the image wall.jpg from the "images" directory.
           The Output generated will be an image of jpg type.
           And The Output generated will BlackWHite / GrayScaled.
           And The Output generated named 'wall_BW_art.jpg' will be stored in "output" directory.

    ''')


if __name__ == "__main__":
    if len(argv) == 4:

        file = argv[1]
        output_type = int(argv[2])
        mode = int(argv[3])

        if mode not in mode_types or output_type not in types:
            print_usage()
            exit(0)  # Invalid Argument Case

        image = Image.open(file).convert('RGB')
        basename = os.path.basename(file)
        filename, ext = os.path.splitext(basename)

        initialize()

        generate_output(output_type, filename, image, mode)

    else:
        print_usage()
