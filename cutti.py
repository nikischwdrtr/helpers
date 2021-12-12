# for cutting videos into segments

import os
import subprocess
import math

# path shizzle
path = "./"
directory = "exports"
files = os.listdir(path)
length = 0
howmany = 0
getVideo = []

print(' /$$   /$$ /$$$$$$ /$$   /$$ /$$$$$$       /$$   /$$ /$$$$$$ /$$   /$$  /$$$$$$')
print('| $$$ | $$|_  $$_/| $$  /$$/|_  $$_/      | $$  /$$/|_  $$_/| $$$ | $$ /$$__  $$')
print('| $$$$| $$  | $$  | $$ /$$/   | $$        | $$ /$$/   | $$  | $$$$| $$| $$  \__/')
print('| $$ $$ $$  | $$  | $$$$$/    | $$        | $$$$$/    | $$  | $$ $$ $$| $$ /$$$$')
print('| $$  $$$$  | $$  | $$  $$    | $$        | $$  $$    | $$  | $$  $$$$| $$|_  $$')
print('| $$\  $$$  | $$  | $$\  $$   | $$        | $$\  $$   | $$  | $$\  $$$| $$  \ $$')
print('| $$ \  $$ /$$$$$$| $$ \  $$ /$$$$$$      | $$ \  $$ /$$$$$$| $$ \  $$|  $$$$$$/')
print('|__/  \__/|______/|__/  \__/|______/      |__/  \__/|______/|__/  \__/ \______/ ')
print('')
print('')
print('')
print('')
print('')

# create new folder
newpath = os.path.join(path, directory)
os.mkdir(newpath)
print newpath+" has been created breeeee..."

# get video
for filename in os.listdir(path):
    if filename.endswith(".avi") or filename.endswith(".mp4") or filename.endswith(".mov"):
        getVideo.append(filename)
    else:
        continue
print "found your video file hehehe "+getVideo[0]

# convert video
os.system("ffmpeg -i "+getVideo[0]+" new.avi")

# get video length
lengths = os.popen("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 new.avi").readlines()
lenghtoflentghts = len(lengths[0])
minusaids = lengths[0][:lenghtoflentghts - 2]
os.system("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 -sexagesimal new.avi")
print "..is your video long GGGGggggg..."

# calculate how many videos
howv = float(minusaids)/30
rhowv = math.ceil(howv)
print rhowv," videos will be creeated (this will take some time....)"

# cut video in 30s parts
start = 0
end = 30
name = 1
print "**************************************************************************************"
print ""
print "                 NOW SOME WEIRD STUFF NOBODY GETS IS HAPPENING!!!"
print "**************************************************************************************"
print ""
for filename in os.listdir(path):
    for x in range(int(rhowv)):
        if filename.endswith(".avi"):
            os.system("ffmpeg -i "+getVideo[0]+" -ss "+str(start)+" -t "+str(end)+" "+newpath+"/"+str(name)+".avi")
            start += 30
            name += 1
        else:
            continue
print ""
print "**************************************************************************************"
print "                             NOW THIS SHIT IS GONE THX"
print "**************************************************************************************"
print ""
howmany = os.listdir(newpath)
print len(howmany), " videos are created, now get work silly :))))"
