import LCD_1in44
import os,shutil,time,argparse
from PIL import Image

# lcd init
LCD = LCD_1in44.LCD()
Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT
LCD.LCD_Init(Lcd_ScanDir)
LCD.LCD_Clear()

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i',type=str,help='enter video path',required=True)
parser.add_argument('-fr',type=str,help='enter framerate',required=True)
parser.add_argument('-vw',type=str,help='enter video width',required=True)
parser.add_argument('-vh',type=str,help='enter video height',required=True)
args = parser.parse_args()
video = args.i
frameRate = float(args.fr)
w = args.vw
h = args.vh

# remove temp folder if still exists
if os.path.exists('frames'):
    shutil.rmtree("frames")

## functions
# change video resolution to display
def videoResize():
    os.system('ffmpeg -y -i '+video+' -vf scale='+w+':'+h+',setsar=1 '+video[:-4]+'_resized.mp4 -hide_banner -loglevel panic')
# extract frames from video
def extract_frames():
    videoFile = video[:-4]+'_resized.mp4'
    os.makedirs("frames")
    os.system('ffmpeg -i '+videoFile+' "frames/%07d.jpg" -hide_banner -loglevel panic')
# show frames on display
def showFrames():
    frames = os.listdir('frames')
    frames.sort()
    while True:
        for x in frames:
            image = Image.open('frames/'+x)
            print(x)
            LCD.LCD_ShowImage(image,0,0)
            time.sleep(1/frameRate)

# run functions
videoResize()
extract_frames()
showFrames()