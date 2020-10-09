import os
import numpy as np 
import cv2
from imageio import imread
import re
from matplotlib import pyplot as plt
from skimage import morphology, img_as_float
from scipy.signal import find_peaks
import json

os.chdir('/Users/pedroflores')
dir = os.getcwd()
print(dir)

pathIn = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020-skeletons/Hemiplegic/s23/skeletons/front_view/'
pathInSide = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020-skeletons/Hemiplegic/s23/skeletons/side_view/'
pathInPose = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020-skeletons/Hemiplegic/s23/pose/front_view/'

def sort_nicely( l ):
    # Sort the given list in the way that humans expect.
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )


folders = [folder for folder in os.listdir(pathIn) if '_' in folder and '.DS' not in folder]
sort_nicely(folders)

for folder in folders:
    print(folder)

    pathFolder = os.path.join(pathIn,folder)
    pathFolderSide = os.path.join(pathInSide,folder)
    
    frames = [f for f in os.listdir(pathFolder) if 'DS' not in f]
    sort_nicely(frames)

    framesSide = [f for f in os.listdir(pathFolderSide) if 'DS' not in f]
    sort_nicely(framesSide)

    for frame in frames:
        if 'DS' in frame:
            continue

        if frame not in framesSide:
            os.remove(os.path.join(pathFolder,frame))

        # if frame in framesSide:
        #     for lvl in ['lvl1', 'lvl2']:
        #         if lvl in folder:
        #             poseFolderPath = os.path.join(pathInPose, 's1pat4' + lvl)
        #             poseJSONs = os.listdir(poseFolderPath)

        #             frameNumber = frame.replace('.png','')
        #             pose = [p for p in poseJSONs if frameNumber.zfill(12) in p]
        #             posePath = os.path.join(poseFolderPath,pose[0])

        #             with open(posePath) as json_file:
        #                 dic = json.load(json_file)

        #             # feet = dic["part_candidates"][0]["19"] and dic["part_candidates"][0]["20"] and dic["part_candidates"][0]["21"] and dic["part_candidates"][0]["22"] and dic["part_candidates"][0]["23"] and dic["part_candidates"][0]["24"]
        #             feet = dic["part_candidates"][0]["11"] and dic["part_candidates"][0]["14"]
                    
        #             if not feet:
        #                 os.remove(os.path.join(pathFolder,frame))
        # else:
        #     os.remove(os.path.join(pathFolder,frame))

        # lisboa luanda budapeste madrid maputo