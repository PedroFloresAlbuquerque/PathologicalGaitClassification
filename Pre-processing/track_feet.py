import os
import numpy as np 
import cv2
from imageio import imread
import re
from matplotlib import pyplot as plt
from skimage import morphology, img_as_float

os.chdir('/Users/pedroflores')
dir = os.getcwd()
print(dir)

pathIn = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Front Binary Frames/'

def sort_nicely( l ):
    # Sort the given list in the way that humans expect.
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

frames = os.listdir(pathIn)
sort_nicely(frames)

imgs_array = [cv2.imread(pathIn + frame, 0) for frame in frames if 'DS' not in frame]

step_width = []

count = 0
for image in imgs_array:

    # Rows from lower quarter of image
    l_4 = (np.shape(image)[0]//4)*3

    # Get lower quarter of image
    image_l_4 = image[l_4:,:]  

    if sum(sum(image_l_4)) < 2000:
        continue

    # Mean across all columns and their indices
    column_means = image_l_4.mean(axis=0)
    nonzero_idx = np.nonzero(column_means)

    # Get first and last columns with active pixels
    f_c = nonzero_idx[0][0]
    l_c = nonzero_idx[0][-1]

    cv2.rectangle(image,(f_c,l_4),(l_c,np.shape(image)[0]), 255, thickness=2)
    cv2.imshow('',image)
    cv2.waitKey(100)

    step_width.append(l_c - f_c)

    count += 1

plt.plot(step_width)
plt.show()