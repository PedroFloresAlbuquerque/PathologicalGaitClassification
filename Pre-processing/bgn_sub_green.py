import os
import numpy as np 
import cv2
from imageio import imread
import re
from matplotlib import pyplot as plt
from skimage import morphology
from scipy.ndimage import label

os.chdir('/Users/pedroflores')
dir = os.getcwd()
print(dir)

pathIn = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Front Frames/'
pathOut = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Front Binary Frames'

def sort_nicely( l ):
    # Sort the given list in the way that humans expect.
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

frames = os.listdir(pathIn)
sort_nicely(frames)
frames.pop(0)

count = 0
for frame in frames:
    
    try:

        image = cv2.imread(pathIn + frame)

        hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        # # Front
        # low_green = np.array([60, 130, 90])
        # high_green = np.array([67, 255, 255])

        # Side
        low_green = np.array([58, 100, 90])
        high_green = np.array([67, 255, 255])
        
        fgmask = cv2.inRange(hsv_image, low_green, high_green)
        fgmask = np.ones((np.shape(image)[0],np.shape(image)[1]),dtype=fgmask.dtype) * fgmask.max() - fgmask

        kernel = np.ones((6,6),np.uint8)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

        kernel = np.ones((6,6),np.uint8)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

        label_mask, num_labels = label(fgmask)
        fgmask = fgmask * morphology.remove_small_objects(label_mask, 10000)

        if count == 300:
            break

        if count < 50:
            count += 1
            continue

        # if 'frame' in frame:
        plt.imsave(pathOut + "/frame%d.jpg" % count, fgmask,cmap='gray')
        count += 1

    except (IOError, SyntaxError, cv2.error):
        print('Bad file:', frame)