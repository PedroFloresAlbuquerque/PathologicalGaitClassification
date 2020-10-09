import os
import numpy as np 
import cv2
from imageio import imread
from PIL import Image
import re
from sort import sort_nicely

os.chdir('/Users/pedroflores')
dir = os.getcwd()
print(dir)

pathIn = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Side Frames/'
pathOut = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Side Binary Frames'

fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=50)

frames = os.listdir(pathIn)
sort_nicely(frames)

count = 0
for frame in frames:
    
    try:
        image = Image.open(pathIn + frame)
        image = np.array(image)
        
        fgmask = fgbg.apply(image)
        fgmask = (fgmask != 127) * fgmask
        kernel = np.ones((6,6),np.uint8)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
        # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

        if 'frame' in frame:
            cv2.imwrite( pathOut + "/frame%d.jpg" % count, fgmask)
            count += 1

    except (IOError, SyntaxError):
        print('Bad file:', frame)