import sys
import argparse
import os
import cv2

# os.chdir('/Users/pedroflores')
# dir = os.getcwd()
# print(dir)

# pathIn = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Video/Side17.mpg'
# pathOut = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Front Frames'


def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*100))    # added this line 
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        if success: cv2.imwrite( pathOut + "/frame%d.jpg" % count, image)     # save frame as JPEG file
        count = count + 1

from matplotlib import pyplot as plt

def extractFrames(pathIn):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success = True
    frames = []
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*100))    # added this line 
        success,frame = vidcap.read()
        # print ('Read a new frame: ', success)
        if success: frames.append(frame)
        count = count + 1
    return frames

# extractImages(pathIn,pathOut)

# extractFrames(pathIn)