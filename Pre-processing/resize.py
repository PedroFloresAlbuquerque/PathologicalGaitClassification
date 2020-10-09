import os
import numpy as np 
import cv2
# from imageio import imread
from PIL import Image
import re
from skimage.measure import regionprops
from sort import sort_nicely
from matplotlib import pyplot as plt
from skimage import img_as_ubyte

# os.chdir('/Users/pedroflores')
# dir = os.getcwd()
# print(dir)

# pathIn = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/'
# pathOut = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020'

def mass_center(img,is_round=True):
    Y = img.mean(axis=1)
    X = img.mean(axis=0)
    Y_ = np.sum(np.arange(Y.shape[0]) * Y)/np.sum(Y)
    X_ = np.sum(np.arange(X.shape[0]) * X)/np.sum(X)
    if is_round:
        return int(round(X_)),int(round(Y_))
    return X_,Y_

def resize(images, pathOut):

    count = 0
    for image in images:

        if image.dtype != 'uint8':
            # try:
            print(image.dtype)
            image = img_as_ubyte(image)
            # except ValueError:
            #     continue

        x,y,w,h = cv2.boundingRect(image)

        if h == 0 or w == 0:
            count += 1
            continue

        x_c, y_c = mass_center(image)

        padded = np.zeros((h,h),dtype=np.uint8)
        x_l = h//2-x_c+x
        x_r = h//2+w-x_c+x

        if h < x_r or x_l < 0:
            count += 1
            continue

        padded[:,x_l:x_r] = image[y:y+h,x:x+w]
        resized_image = np.array(Image.fromarray(padded).resize((224,224)))

        # plt.imshow(resized_image)
        # plt.show()
        cv2.imwrite( pathOut + "/frame%d.jpg" % count, resized_image)
        count += 1
    
    return count

def resize_skel(image, cen):

    if image.dtype != 'uint8':
        # try:
        print(image.dtype)
        image = img_as_ubyte(image)
        # except ValueError:
        #     continue

    x,y,w,h = cv2.boundingRect(image)

    if h == 0 or w == 0:
        resized_image = np.zeros((224,224,1), np.uint8)
        return resized_image

    print('cen:', cen)

    cen = cen.astype(np.int)

    padded = np.zeros((h,h),dtype=np.uint8)
    x_l = h//2-cen+x
    x_r = h//2+w-cen+x

    print('x_l:', x_l, 'x_r:', x_r, 'cen:', cen)

    padded[:,x_l:x_r] = image[y:y+h,x:x+w]
    resized_image = np.array(Image.fromarray(padded).resize((224,224)))
    
    return resized_image