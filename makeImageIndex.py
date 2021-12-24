# tool which lists all images (jpg/png/gif) in a folder
# it puts it in new text file 
# perfectly formatted for javascript array objects

import glob
import os
from PIL import Image

# choose folder
mydir = "./"

# get list of files
jpg_list = glob.glob(mydir + "*.jpg")
jpgbig_list = glob.glob(mydir + "*.JPG")
png_list = glob.glob(mydir + "*.png")
gif_list = glob.glob(mydir + "*.gif")

# get list of resolution
jpg_reso = []
for x in range(len(jpg_list)):
    img = Image.open(jpg_list[x])
    width, height = img.size
    jpg_reso.append(str(width)+'x'+str(height))
jpgbig_reso = []
for x in range(len(jpgbig_list)):
    img = Image.open(jpgbig_list[x])
    width, height = img.size
    jpgbig_reso.append(str(width)+'x'+str(height))
png_reso = []
for x in range(len(png_list)):
    img = Image.open(png_list[x])
    width, height = img.size
    png_reso.append(str(width)+'x'+str(height))
gif_reso = []
for x in range(len(gif_list)):
    img = Image.open(gif_list[x])
    width, height = img.size
    gif_reso.append(str(width)+'x'+str(height))

# get list of size
jpg_size = []
for x in range(len(jpg_list)):
    img = os.path.getsize(jpg_list[x])
    jpg_size.append(str(round(img/1000))+'kb')
jpgbig_size = []
for x in range(len(jpgbig_list)):
    img = os.path.getsize(jpgbig_list[x])
    jpgbig_size.append(str(round(img/1000))+'kb')
png_size = []
for x in range(len(png_list)):
    img = os.path.getsize(png_list[x])
    png_size.append(str(round(img/1000))+'kb')
gif_size = []
for x in range(len(gif_list)):
    img = os.path.getsize(gif_list[x])
    gif_size.append(str(round(img/1000))+'kb')

# clean file name list
jpg_list = [e[2:] for e in jpg_list]
jpgbig_list = [e[2:] for e in jpgbig_list]
png_list = [e[2:] for e in png_list]
gif_list = [e[2:] for e in gif_list]

# join lists
imageNames = jpg_list + jpgbig_list + png_list + gif_list
imageSizes = jpg_size + jpgbig_size + png_size + gif_size
imageResos = jpg_reso + jpgbig_reso + png_reso + gif_reso

# create txt file
f = open("!ImageIndex.txt","w+")

# write txt file
for x in range(len(imageNames)):
    f.write("{ \n")
    f.write("   id: "+str(x+1)+", \n")
    f.write("   src: 'images/archive/"+imageNames[x]+"', \n")
    f.write("   title: '"+imageNames[x]+"', \n")
    f.write("   size: '"+imageSizes[x]+"', \n")
    f.write("   reso: '"+imageResos[x]+"', \n")
    f.write("}, \n")
f.close()