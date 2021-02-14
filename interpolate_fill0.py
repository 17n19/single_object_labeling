import cv2, os, sys
import argparse
import imutils
from imutils.video import count_frames


# parse the arguments used to call this script
parser = argparse.ArgumentParser()
parser.add_argument('--name', help='name of video file', type=str)
args = parser.parse_args()
fname =  os.path.basename(args.name)[:-4] #filename without extentsion
video = cv2.VideoCapture(args.name) # Read video
name = fname

total_frames = count_frames(args.name)


# create directories to store individual frames and their labels
#os.makedirs("./labels", exist_ok=True)
#os.makedirs("./images", exist_ok=True)
f = open('./labels/' + name + '_2.txt', "r")
f2 = open('./labels/' + name + '_2_2.txt', "a")

count_frame = 0
out = False

for lines in f:
    line = lines
    if line == "":
        break
    f2.write(line)
    count_frame = count_frame + 1

while count_frame <= total_frames:
    line = "0,0,0,0\n"
    f2.write(line)
    count_frame = count_frame + 1
        






