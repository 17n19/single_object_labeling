# single_object_labeling
Labeling tool for single object tracking 

You can draw a bounding box on your interested object in each frame and the raw coordinates `x, y, w, h` of the bounding boxes wil be written on single `.txt` file.

And you can also choose number of frame to be `interpolated`

Code is edited from https://github.com/sachinruk/Video_bbox

## Dependencies :
  - Python 3.5.5+
  - OpenCV 3.4.3+
  - Imutils 0.5.4+
  
## Docker container :
   *you can check docker commands guide for Linux and Windows at https://hub.docker.com/r/mintjitlada/sodt* 
     
    docker pull mintjitlada/sodt:label
  
    
## Command : 
    python single_object_label.py --name <path to video file>                                      

## How to use :
  1. If you have finished drawing box, press `space bar` twice for comfirmation (you can re-draw as many as you can until you press `space bar` twice, only the last drawing will be written)
  2. If there are no interested object in current frame and you want to pass `0,0,0,0` to `.txt` at current index, just press `space bar` `twice`
  3. If there are no interested object in the video anymore and you want to pass `0,0,0,0` to the rest of `.txt`, just press `space bar` `once` and then press `d` which stands for *DONE*
  4. If you want to exit the program just press `q` which stands for *QUIT*
 
 
