# import the image class

import os, sys
from PIL import Image, ImageFilter
import time


# reading and writing images
def display_img(image_li):
    """to display images. It accepts a list of image file"""
    if len(image_li) != 0:
        print(f"There are {len(image_li)} images \n")
        for image in image_li:
            im = Image.open(image)
            print(im.format, im.size, im.mode)
            im.show()
            time.sleep(3)
            im.close()
    else:
        print("iterable cannot not be empty")


# convert jpeg to png
def convert_img():
    with Image.open("./pokydex/squirtle.jpg") as squirtle:
        converted_img = squirtle.convert('L')
        converted_img.save("./converted_images/grey_squirtle.png", 'png')
        print('Image converted and saved.')


# convert files to jpeg
def file_converter():
    for infile in sys.argv[1:]:
        f, e = os.path.split(infile)
        outfile = f + ".jpg"
        if infile != outfile:
            try:
                with Image.open(infile) as im:
                    im.save(outfile)
            except IOError:
                print("cannot convert", infile)


def get_filters(image):
    filters = dir(ImageFilter)
    try:
        if image:
            image = str(image)
            with Image.open(image) as im:
                filtered_img = im.filter(ImageFilter.BLUR)
                print('Filter added')
                filtered_img.save("./filtered_images/blurred.png", "png")
    except ValueError:
        raise ValueError







