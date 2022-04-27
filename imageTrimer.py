from PIL import Image
from itertools import product
import glob
import os

# folder stuff
mydir = "./"
newdir = "trimed"
path = os.path.join(mydir,newdir)

# create folder
os.mkdir(path)

# get list of images
jpg_list = glob.glob(mydir + "*.jpg")
jpgbig_list = glob.glob(mydir + "*.JPG")
png_list = glob.glob(mydir + "*.png")

# trim function
def trim(image):
    img = Image.open(image)
    # choose crop size
    w, h = img.size
    l = 75
    t = 0
    r = w
    b = h

    img2 = img.crop((l,t,r,b))
    img2.save(os.path.join(path+image[1:]))

# trim images
for x in range(len(jpg_list)):
    trim(jpg_list[x])
for x in range(len(jpgbig_list)):
    trim(jpgbig_list[x])
for x in range(len(png_list)):
    trim(png_list[x])