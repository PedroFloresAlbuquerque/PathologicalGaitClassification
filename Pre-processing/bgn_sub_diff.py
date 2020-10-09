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

# pathIn = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Side Frames/'
# pathOut = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Side Binary Frames'

pathIn = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Front Frames/'
pathOut = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Front Binary Frames'

pathBGN = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/Background Frames/'

def sort_nicely( l ):
    # Sort the given list in the way that humans expect.
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )


front_background_light = Image.open(pathBGN + 'front_bgn_light.jpg')
front_background_light = np.array(front_background_light)
front_background_dark = Image.open(pathBGN + 'front_bgn_dark.jpg')
front_background_dark = np.array(front_background_dark)

frames = os.listdir(pathIn)
sort_nicely(frames)

count = 0
for frame in frames:
    
    try:
        # Load image and convert to numpy array
        image = Image.open(pathIn + frame)
        image = np.array(image)
        
        diff = abs(image.astype(int) - front_background_light.astype(int))
        diff2 = abs(image.astype(int) - front_background_dark.astype(int))

        fgmask = np.ones((np.shape(image)[0],np.shape(image)[1]))
        fgmask = (np.linalg.norm(diff, axis=2) > 60) * fgmask
        fgmask = (np.linalg.norm(diff2, axis=2) > 20) * fgmask

        kernel = np.ones((10,10),np.uint8)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

        print(fgmask.dtype)

        nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(fgmask.astype(np.uint8), connectivity=8)
        sizes = stats[1:, -1]; nb_components = nb_components - 1

        min_size = 500

        #your answer image
        img2 = np.zeros((output.shape))
        #for every component in the image, you keep it only if it's above min_size
        for i in range(0, nb_components):
            if sizes[i] >= min_size:
                img2[output == i + 1] = 255

        # print(np.linalg.norm(diff, axis=2).mean())

        if 'frame' in frame:
            plt.imsave(pathOut + "/frame%d.jpg" % count, img2,cmap='gray')
            count += 1

        if count == 200:
            break

    except (IOError, SyntaxError, cv2.error):
        print('Bad file:', frame)