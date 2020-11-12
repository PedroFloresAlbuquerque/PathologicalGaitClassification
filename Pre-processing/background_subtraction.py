import os
import numpy as np 
import cv2
import re
from sort import sort_nicely
from scipy.ndimage import label
from skimage import morphology, img_as_ubyte
from matplotlib import pyplot as plt

def bgn_sub_MOG(frames):

    masks = []
    fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=50)
    count = 0
    
    for frame in frames:
        
        try:
            
            fgmask = fgbg.apply(frame)
            fgmask = (fgmask != 127) * fgmask
            kernel = np.ones((6,6),np.uint8)
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
            # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

            masks.append(fgmask)

        except (IOError, SyntaxError):
            print('Bad file:', frame)
    
    return masks

def bgn_sub_green_front_28(frames):

    masks = []
    count = 0
    for frame in frames:
        
        try:

            hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

            low_green = np.array([60, 130, 90])
            high_green = np.array([67, 255, 255])
            fgmask = cv2.inRange(hsv_image, low_green, high_green)
            fgmask = np.ones((np.shape(frame)[0],np.shape(frame)[1]),dtype=fgmask.dtype) * fgmask.max() - fgmask

            kernel = np.ones((6,6),np.uint8)
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

            kernel = np.ones((6,6),np.uint8)
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

            label_mask, num_labels = label(fgmask,output=fgmask.dtype)
            fgmask = fgmask * morphology.remove_small_objects(label_mask, 10000)

            masks.append(fgmask)

        except (IOError, SyntaxError, cv2.error):
            print('Bad file:', frame)

    return masks


def bgn_sub_green_front_02(frames):

    masks = []
    count = 0
    for frame in frames:
        
        try:

            hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

            low_green = np.array([60, 130, 125])
            high_green = np.array([67, 255, 255])
            fgmask = cv2.inRange(hsv_image, low_green, high_green)
            fgmask = np.ones((np.shape(frame)[0],np.shape(frame)[1]),dtype=fgmask.dtype) * fgmask.max() - fgmask

            kernel = np.ones((6,6),np.uint8)
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

            kernel = np.ones((6,6),np.uint8)
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

            label_mask, num_labels = label(fgmask,output=fgmask.dtype)
            fgmask = fgmask * morphology.remove_small_objects(label_mask, 10000)

            masks.append(fgmask)

        except (IOError, SyntaxError, cv2.error):
            print('Bad file:', frame)

    return masks


def bgn_sub_green_side(frames):

    masks = []
    count = 0
    for frame in frames:
        
        try:

            hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

            low_green = np.array([58, 100, 90])
            high_green = np.array([67, 255, 255])
            fgmask = cv2.inRange(hsv_image, low_green, high_green)
            fgmask = np.ones((np.shape(frame)[0],np.shape(frame)[1]),dtype=fgmask.dtype) * fgmask.max() - fgmask

            kernel = np.ones((6,6),np.uint8)
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

            kernel = np.ones((6,6),np.uint8)
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

            label_mask, num_labels = label(fgmask,output=fgmask.dtype)
            fgmask = fgmask * morphology.remove_small_objects(label_mask, 10000)

            masks.append(fgmask)

        except (IOError, SyntaxError, cv2.error):
            print('Bad file:', frame)

    return masks


def bgn_sub_green_side_silhouettes(frames):

    masks = []
    silhouettes = []
    count = 0
    for frame in frames:
        
        try:

            hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

            low_green = np.array([58, 100, 90])
            high_green = np.array([67, 255, 255])
            fgmask = cv2.inRange(hsv_image, low_green, high_green)
            fgmask = np.ones((np.shape(frame)[0],np.shape(frame)[1]),dtype=fgmask.dtype) * fgmask.max() - fgmask

            kernel = np.ones((6,6),np.uint8)
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

            kernel = np.ones((6,6),np.uint8)
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

            label_mask, num_labels = label(fgmask,output=fgmask.dtype)
            fgmask = fgmask * morphology.remove_small_objects(label_mask, 10000)

            masks.append(fgmask)
            silhouette = np.zeros(np.shape(frame)[0],np.shape(frame)[1],np.shape(frame)[2])
            silhouette[:,:,0] = frame[:,:,0] * fgmask; silhouette[:,:,1] = frame[:,:,1] * fgmask; silhouette[:,:,1] = frame[:,:,1] * fgmask
            silhouettes.append(silhouette)

        except (IOError, SyntaxError, cv2.error):
            print('Bad file:', frame)

    return masks, silhouettes