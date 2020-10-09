import os
import numpy as np 
import cv2
from imageio import imread
from PIL import Image
import re
from matplotlib import pyplot as plt

os.chdir('/Users/pedroflores')
dir = os.getcwd()
print(dir)

pathBGN = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020-Background/Background Frames/'

def sort_nicely( l ):
    # Sort the given list in the way that humans expect.
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

pathIn = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020-Background/s1/Side Frames/'

front_frame = cv2.imread(pathIn + 'frame70.jpg')
hsv_front_frame = cv2.cvtColor(front_frame,cv2.COLOR_BGR2HSV)

hue = hsv_front_frame[:,:,0].flatten()
sat = hsv_front_frame[:,:,1].flatten()
val = hsv_front_frame[:,:,2].flatten()

plt.xlabel('Hue', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.hist(hue, bins=50)
plt.suptitle('Side Frame Hue Histogram', fontsize=14, fontweight='bold')
# plt.savefig('Documents/IST/Tese/DATASETS/GAIT-IST-2020-Background/s1/Histograms/hsv_front_frame57')
plt.show()s