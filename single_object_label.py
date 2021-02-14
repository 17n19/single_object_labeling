import cv2, os, sys
import argparse
import imutils
from imutils.video import count_frames


# parse the arguments used to call this script
parser = argparse.ArgumentParser()
parser.add_argument('--name', help='name of video file', type=str)
parser.add_argument('--max_obj', help='Maximum number of objects followed', type=int, default=6)
parser.add_argument('--max_frames', help='Maximum number of objects followed', type=int, default=500)
parser.add_argument('--thresh', help='Threshold for scene changes', type=float, default=2)
args = parser.parse_args()
max_obj = args.max_obj
max_frames = args.max_frames
thresh = args.thresh
total_frames = count_frames(args.name)
print("[INFO] Number of frames : "+ str(total_frames))
fname =  os.path.basename(args.name)[:-4] #filename without extentsion
video = cv2.VideoCapture(args.name) # Read video
name = fname

# create directories to store individual frames and their labels
os.makedirs("./labels", exist_ok=True)
f = open('./labels/' + name + '.txt', "a")
#os.makedirs("./images", exist_ok=True)
os.makedirs("./images/"+name, exist_ok=True)
# Exit if video not opened
if not video.isOpened():
    print("Could not open video")
    sys.exit()
 
# Read first frame
ok,frame = video.read()
if not ok:
    print("Cannot read video file")
    sys.exit()

h, w, _ = frame.shape
# import pdb; pdb.set_trace()
#h = w = 608
initBB = None

frames = 1
prev_mean = 0

nobox = False
box = False
out = False
skip = False

while ok or frames <= total_frames:
    nobox = False
    box = False
    if out == True:
        #line = "0,0,0,0\n"
        print(str(frames).zfill(4),0,0,0,0)
        f.write(line)
        frames += 1
        ok,frame = video.read()
        continue

    #frame_diff = abs(frame.mean() - prev_mean)
    #prev_mean = frame.mean()

    #frame = cv2.resize(frame, (h, w))
    name_img = fname + '_' + str(frames).zfill(4)
    origFrame = frame.copy()
    
    
    # if the 'd' key is selected, we are going to "select" a bounding
    # box to track
    # select the bounding box of the object we want to track (make
    # sure you press ENTER or SPACE after selecting the ROI)
    initBB = cv2.selectROI("Frame", frame, fromCenter=False) 
    # create a new object tracker for the bounding box and add it
    # to our multi-object tracker
    if initBB[2] == 0 or initBB[3] == 0: # if no width or height
        nobox = True
    else :
        box = True

    #key = cv2.waitKey(0) & 0xFF
    key = cv2.waitKey(0)
    #if key == ord("s"):
    if key%256 == 32: # spacebar to next frame
        if nobox == True:      
            #cv2.imwrite('./images/' + name + '/'+ name_img + '.jpg', origFrame)
            print(str(frames).zfill(4),0,0,0,0)
            f.write(str(0) + "," + str(0) + "," + str(0) + "," + str(0)+"\n")
        elif box == True:
            #cv2.imwrite('./images/' + name + '/'+ name_img + '.jpg', origFrame)
            print(str(frames).zfill(4),initBB[0],initBB[1],initBB[2],initBB[3])
            f.write(str(initBB[0]) + "," + str(initBB[1]) + "," + str(initBB[2]) + "," + str(initBB[3])+"\n")
    elif key & 0xFF == ord("d"):
        out = True
        line = "0,0,0,0\n"
        print(str(frames).zfill(4),0,0,0,0)
        f.write(line)
        frames += 1
        ok,frame = video.read()
        continue
        #break
    elif key == ord("q"):
        break

    cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
    cv2.imshow("Frame", frame)

    #interpolate next 5 frame
    for i in range(5):
        frames += 1
        ok,frame = video.read()
        if not ok or frame is None:
            if box == True :
                line = str(initBB[0]) + "," + str(initBB[1]) + "," + str(initBB[2]) + "," + str(initBB[3])+"\n"
            elif nobox == True:
                line = "0,0,0,0\n"
            out = True
            skip = True
            break
        name_img = fname + '_' + str(frames).zfill(4)
        origFrame = frame.copy()
        if nobox == True : 
            #cv2.imwrite('./images/' + name + '/'+ name_img + '.jpg', origFrame)
            print(str(frames).zfill(4),0,0,0,0)
            f.write(str(0) + "," + str(0) + "," + str(0) + "," + str(0)+"\n")
        elif box == True:
            #cv2.imwrite('./images/' + name + '/'+ name_img + '.jpg', origFrame)
            print(str(frames).zfill(4),initBB[0],initBB[1],initBB[2],initBB[3])
            f.write(str(initBB[0]) + "," + str(initBB[1]) + "," + str(initBB[2]) + "," + str(initBB[3])+"\n")
    if skip:
        continue
    frames += 1
    ok,frame = video.read()
video.release()
# close all windows
cv2.destroyAllWindows()