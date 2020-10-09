import sys
# Get path to directory with functions for dataset processing
sys.path.append('/Users/pedroflores/Documents/IST/Tese/Code')
import numpy as np
import glob
import cv2 as cv
import os
import json
import math
import itertools
from sort import sort_nicely
import resize

def pairwise(it):
    it = iter(it)
    while True:
        yield next(it), next(it)

def connect(img, x, y, a, b):
    if x[a] and x[b] and y[a] and y[b]:
        cv.line(img,(x[a],y[a]),(x[b],y[b]),(255),13)

def draw_skeleton(dic, aa, bb):
    if len(dic["people"]):

        if len(dic["people"]) > 1:
            a = np.vstack(tuple(dic["people"][p]["pose_keypoints_2d"] for p in range(len(dic["people"]))))
            if sum([x.dot(y) for x, y in itertools.combinations(a, 2)]) == 0:
                coord = np.sum(a, axis = 0)
                coord = coord.tolist()
            else:
                coord = dic["people"][0]["pose_keypoints_2d"]
        else:
            coord = dic["people"][0]["pose_keypoints_2d"]

        del coord[2::3]
        coord = [round(x) for x in coord]

        x = coord[0::2]
        y = coord[1::2]

        xmin = min([i for i in x if i !=0])
        xmax = max(x)
        ymin = min([i for i in y if i !=0])
        ymax = max(y)

        h = ymax - ymin
        w = xmax - xmin

        cen = np.mean([x[1], x[8]])
        shift = round((np.mean([xmax, xmin]) - cen)*(7/40))

        if (xmin < xmax) and (ymin < ymax) and ((h-224)/h < w):

            img = np.zeros((720, 1280), np.uint8)

            for i in range(len(aa)-1):
                connect(img, x, y, aa[i], bb[i])

            img = resize.resize_skel(img, cen)

        else:
            img = np.zeros((224,224), np.uint8)
    else:
        img = np.zeros((224,224), np.uint8)

    # cv.imshow("image", img)
    # k = cv.waitKey(1) & 0xff
    # if k == ord("p"):
    #     cv2.waitKey(0)

    return img

def main():

    aa = [0, 0, 0, 15, 16, 1, 2, 3, 1, 5, 6, 1, 8, 9, 10, 11, 11, 22, 8, 12, 13, 14, 14, 19]
    bb = [1, 15, 16, 17, 18, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 24, 22, 23, 12, 13, 14, 21, 19, 20]

    os.chdir('/Users/pedroflores')
    print(os.getcwd())

    location = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/pose2/'
    pathOut = 'Documents/IST/Tese/DATASETS/GAIT-IST-2020/skel/'

    f = 1

    filenames = os.listdir(location)
    sort_nicely(filenames)
    for filename in filenames:
        if filename.endswith('.json'):
            with open(location + filename) as json_file:
                dic = json.load(json_file)
            img = draw_skeleton(dic, aa, bb)

            cv.imwrite(pathOut+str(f).zfill(6)+".png", img)
            f += 1



if __name__ == '__main__':
    main()
