import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from imageio import imread
import re
from PIL import Image
import scipy
from scipy.spatial import distance
import math
from math import sqrt
from scipy.signal import savgol_filter, argrelextrema, find_peaks
from scipy.ndimage import gaussian_filter1d
from math import ceil

def sort_nicely( l ):
    # Sort the given list in the way that humans expect.
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

# Lists with pathologies and subjects
pathologies = {'Diplegic': 'pat1', 'Hemiplegic': 'pat2', 'Neuropathic': 'pat3', 'Normal': 'normal', 'Parkinson': 'pat4'}

cameras = {'Camera 1': 'front_view', 'Camera 3': 'side_view'}

severity2lvl = {'s1': 'lvl1', 's2': 'lvl2', 'Normal': ''}

path = "/Users/pedroflores/Documents/IST/Tese/DATASETS/GAIT-IT-2020"
path2 = "/Users/pedroflores/Documents/IST/Tese/DATASETS/GAIT-IT-2"


sequence_frames = {}

# Iterate through pathologies to access each pathology directory
for pathology in pathologies:

    # Create folder path for each pathology in DATASETS directory
    pathology_dir = os.path.join(path, pathology)
    pathology_dir2 = os.path.join(path2, pathology)

    subs = [sub for sub in os.listdir(pathology_dir) if 'DS' not in sub]

    sort_nicely(subs)

    # Iterate folder for each subject in each pathology directory
    for sub in subs:

        # Get folder for subject
        sub_dir = os.path.join(pathology_dir, sub)
        sub_dir2 = os.path.join(pathology_dir2, sub)

        # Get folder for binary silhouettes
        sub_dir_silhouettes = os.path.join(sub_dir, 'silhouettes')
        sub_dir_silhouettes2 = os.path.join(sub_dir2, 'silhouettes')

        # Iterate folder for each view angle in the subject silhouettes directories
        for view in ['front_view','side_view']:

            # Silhouettes
            silhouettes_view_dir = os.path.join(sub_dir_silhouettes, view)
            silhouettes_view_dir2 = os.path.join(sub_dir_silhouettes2, view)

            sequence_folders = [folder for folder in os.listdir(silhouettes_view_dir) if 'DS' not in folder and '.txt' not in folder and '_' in folder]
            sort_nicely(sequence_folders)
            
            sequence_folders2 = [folder for folder in os.listdir(silhouettes_view_dir2) if 'DS' not in folder and '.txt' not in folder and '_' not in folder]
            sort_nicely(sequence_folders2)
            
            # Iterate folder for each severity in the subject silhouettes directories
            for sequence_folder in sequence_folders:

                #print(sequence_folder)

                # Get sequence folders directories
                sequence_folder_dir = os.path.join(silhouettes_view_dir,sequence_folder)
                sequence_folder_dir2 = os.path.join(silhouettes_view_dir2,sequence_folder)

                sequence_folder_dir2lvl1 = os.path.join(silhouettes_view_dir2,sequence_folders2[0])
                frameslvl1 = [frame for frame in os.listdir(sequence_folder_dir2lvl1) if 'DS' not in frame]
                if len(frameslvl1) == 0:
                    print(sequence_folder_dir2lvl1 + ' is empty')
                    continue

                if pathology != 'Normal':
                    sequence_folder_dir2lvl2 = os.path.join(silhouettes_view_dir2,sequence_folders2[1])
                    frameslvl2 = [frame for frame in os.listdir(sequence_folder_dir2lvl2) if 'DS' not in frame]
                    if len(frameslvl2) == 0:
                        print(sequence_folder_dir2lvl2 + ' is empty')
                        continue

                os.mkdir(sequence_folder_dir2)

                # Get binary silhouette sequences
                sequences = [sequence for sequence in os.listdir(sequence_folder_dir) if 'DS' not in sequence]
                sort_nicely(sequences)

                first = sequences[0].replace('frame', '')
                first = first.replace('.jpg','')
                last = sequences[-1].replace('frame', '')
                last = last.replace('.jpg','')

                print("First: ", first, " Last: ", last)

                for frame in range(int(first) * 5, int(last) * 5 + 1):
                    
                    sequence = 'frame' + str(frame) + '.jpg'

                    if 'lvl1' in sequence_folder or pathology == 'Normal':
                        sequence_folder_dir2lvl1 = os.path.join(silhouettes_view_dir2,sequence_folders2[0])
                        os.rename(os.path.join(sequence_folder_dir2lvl1,sequence), os.path.join(sequence_folder_dir2,sequence))
                    elif 'lvl2' in sequence_folder:
                        sequence_folder_dir2lvl2 = os.path.join(silhouettes_view_dir2,sequence_folders2[1])
                        print(sequence_folder_dir2lvl2)
                        os.rename(os.path.join(sequence_folder_dir2lvl2,sequence), os.path.join(sequence_folder_dir2,sequence))
