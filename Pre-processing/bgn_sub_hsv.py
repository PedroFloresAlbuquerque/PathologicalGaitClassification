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

front_background_light = cv2.imread(pathBGN + 'front_bgn_light.jpg')
hsv_front_background_light = cv2.cvtColor(front_background_light,cv2.COLOR_BGR2HSV)
front_background_dark = cv2.imread(pathBGN + 'front_bgn_dark.jpg')
hsv_front_background_dark = cv2.cvtColor(front_background_dark,cv2.COLOR_BGR2HSV)
front_background_shadow = cv2.imread(pathBGN + 'front_bgn_shadow.jpg')
hsv_front_background_shadow = cv2.cvtColor(front_background_shadow,cv2.COLOR_BGR2HSV)
side_background = cv2.imread(pathBGN + 'side_bgn_28.jpg')
hsv_side_background_28 = cv2.cvtColor(side_background,cv2.COLOR_BGR2HSV)
side_background = cv2.imread(pathBGN + 'side_bgn_02.jpg')
hsv_side_background_02 = cv2.cvtColor(side_background,cv2.COLOR_BGR2HSV)

hue = hsv_front_background_light[:,:,0].flatten()
sat = hsv_front_background_light[:,:,1].flatten()
val = hsv_front_background_light[:,:,2].flatten()

f, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(20,5))
ax1.set_title("H")
ax1.hist(hue, bins=50)
ax2.set_title("S")
ax2.hist(sat, bins=50)
ax3.set_title("V")
ax3.hist(val, bins=50)
plt.show()

hue = hsv_front_background_dark[:,:,0].flatten()
sat = hsv_front_background_dark[:,:,1].flatten()
val = hsv_front_background_dark[:,:,2].flatten()

f, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(20,5))
ax1.set_title("H")
ax1.hist(hue, bins=50)
ax2.set_title("S")
ax2.hist(sat, bins=50)
ax3.set_title("V")
ax3.hist(val, bins=50)
plt.show()

hue = hsv_front_background_shadow[:,:,0].flatten()
sat = hsv_front_background_shadow[:,:,1].flatten()
val = hsv_front_background_shadow[:,:,2].flatten()

f, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(20,5))
ax1.set_title("H")
ax1.hist(hue, bins=50)
ax2.set_title("S")
ax2.hist(sat, bins=50)
ax3.set_title("V")
ax3.hist(val, bins=50)
plt.show()

hue = hsv_side_background_28[:,:,0].flatten()
sat = hsv_side_background_28[:,:,1].flatten()
val = hsv_side_background_28[:,:,2].flatten()

f, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(20,5))
ax1.set_title("H")
ax1.hist(hue, bins=50)
ax2.set_title("S")
ax2.hist(sat, bins=50)
ax3.set_title("V")
ax3.hist(val, bins=50)
plt.show()

hue = hsv_side_background_02[:,:,0].flatten()
sat = hsv_side_background_02[:,:,1].flatten()
val = hsv_side_background_02[:,:,2].flatten()

f, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(20,5))
ax1.set_title("H")
ax1.hist(hue, bins=50)
ax2.set_title("S")
ax2.hist(sat, bins=50)
ax3.set_title("V")
ax3.hist(val, bins=50)
plt.show()

# frames = os.listdir(pathIn)
# sort_nicely(frames)

# count = 0
# for frame in frames:
    
#     try:
#         # Load image and convert to hsv
#         image = cv2.imread(pathIn + frame)
#         hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        
#         diff = abs(hsv_image.astype(int) - hsv_front_background_light.astype(int))
#         diff2 = abs(hsv_image.astype(int) - hsv_front_background_dark.astype(int))

#         # fgmask = np.zeros((np.shape(image)[0],np.shape(image)[1]))
#         # fgmask[diff[:,:,0] > 3] = 1
#         # fgmask[diff[:,:,1] > 20] = 1

#         # fgmask = np.ones((np.shape(image)[0],np.shape(image)[1]))
#         # fgmask = (diff[:,:,0] > 3) * fgmask

#         # kernel = np.ones((10,10),np.uint8)
#         # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

#         # kernel = np.ones((5,5),np.uint8)
#         # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

#         # nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(fgmask.astype(np.uint8), connectivity=8)
#         # sizes = stats[1:, -1]; nb_components = nb_components - 1

#         # min_size = 150

#         # #your answer image
#         # img2 = np.zeros((output.shape))
#         # #for every component in the image, you keep it only if it's above min_size
#         # for i in range(0, nb_components):
#         #     if sizes[i] >= min_size:
#         #         img2[output == i + 1] = 255

#         # print(np.linalg.norm(diff, axis=2).mean())

#         if 'frame' in frame:
#             plt.imsave(pathOut + "/frame%d.jpg" % count, fgmask,cmap='gray')
#             count += 1

#         if count == 200:
#             break

#     except (IOError, SyntaxError, cv2.error):
#         print('Bad file:', frame)