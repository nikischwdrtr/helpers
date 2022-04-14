from PIL import Image
from itertools import product
import glob
import os

# how many slices in px
slices = 256

# choose folder
mydir = "./"

# get list of files
jpg_list = glob.glob(mydir + "*.jpg")
jpgbig_list = glob.glob(mydir + "*.JPG")
png_list = glob.glob(mydir + "*.png")

# crop function
def tile(filename, dir_in, dir_out, d):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
        img.crop(box).save(out)

# crop images
for x in range(len(jpg_list)):
    tile(jpg_list[x], mydir, mydir, slices)
for x in range(len(jpgbig_list)):
    tile(jpgbig_list[x], mydir, mydir, slices)
for x in range(len(png_list)):
    tile(png_list[x], mydir, mydir, slices)