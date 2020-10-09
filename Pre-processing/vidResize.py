import sys
# Get path to directory with functions for dataset processing
sys.path.append('/Users/pedroflores/Documents/IST/Tese/Code/Pre-processing')
sys.path.append('/Users/pedroflores/Documents/IST/Tese/Code')
import argparse
import os
import cv2
import numpy as np
import background_subtraction
import resize
import vid2jpg
# from imageio import imread
from PIL import Image
from matplotlib import pyplot as plt
from skimage import morphology
from scipy.ndimage import label
from skimage.measure import regionprops
from sort import sort_nicely

os.chdir('/Users/pedroflores/')

pathIn = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020-Background/s8/IT - Normal-p8- s1 1 (Camera 3).mpg'
pathOut = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020-Background/s8/Side Resized Frames'

# Decompress video into frames
frames = vid2jpg.extractFrames(pathIn)
if 'Camera 1' in pathIn:
    silhouettes = background_subtraction.bgn_sub_green_front_28(frames)
elif 'Camera 3' in pathIn:
    silhouettes = background_subtraction.bgn_sub_green_side(frames)
count = resize.resize(silhouettes, pathOut)