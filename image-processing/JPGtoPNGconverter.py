import sys
import os
from PIL import Image

# grab the first and second argument from the terminal

image_folder = sys.argv[1]
out_folder = sys.argv[2]

print(f"{image_folder} {out_folder}")

# check if output folder exist, if not create it
# using the os or pathlib module
# print(True) if os.path.exists(out_folder) else print(False)
if not os.path.exists(out_folder):
    os.makedirs(out_folder)

# loop through image folder, grap each image,
# convert and safe to the new folder

for filename in os.listdir(image_folder):
    img = Image.open(f'./{image_folder}{filename}')
    image_file = './' + out_folder + filename
    image_file = os.path.splitext(image_file)
    clean_img = image_file[0] + '.png'
    converted_img = img.save(clean_img, 'png')
    print("all done!")

