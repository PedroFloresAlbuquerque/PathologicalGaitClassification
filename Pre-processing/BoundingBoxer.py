import os
import numpy as np 
import cv2
from imageio import imread
from PIL import Image
import re
from matplotlib import pyplot as plt
from skimage import img_as_ubyte

os.chdir('/Users/pedroflores')

# ages = [20, 22, 56, 23, 23, 23, 23, 25, 23, 23, 48, 55, 23, 25, 23, 19, 24, 53, 46, 23, 23]

# plt.hist(ages, bins=40, ec='black')
# plt.xlabel('Age', fontsize=14)
# plt.ylabel('Frequency', fontsize=14)
# plt.title('Subject Age Distribution', fontsize=14, fontweight="bold")
# plt.show()

pathIn = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020-Background/s1/Front Binary Frames/frame57.jpg'

img = cv2.imread(pathIn,cv2.IMREAD_GRAYSCALE)
img = img_as_ubyte(img)
x,y,w,h = cv2.boundingRect(img)
image = np.zeros((720,1280,3))
image[:,:,0] = img; image[:,:,1] = img; image[:,:,2] = img
image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imwrite('Documents/IST/Tese/DATASETS/GAIT-IST-2020-Background/s1/BoundingBoxes/Front57.jpg', image)