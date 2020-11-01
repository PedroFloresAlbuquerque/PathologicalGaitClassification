####### Imports #######
import re
import os
import sys
sys.path.append('/home/pfa/Documents/PathologicalGaitClassification')
import numpy as np
# from keras.applications import Xception
# from keras.models import Model
# from keras.layers import Dense, Input, ConvLSTM2D, GlobalAveragePooling2D, Dropout
# from keras.layers.wrappers import TimeDistributed
# from keras.optimizers import Nadam
# from keras.callbacks import ModelCheckpoint, EarlyStopping
# from keras.preprocessing import image
# from keras.utils import to_categorical
# import matplotlib.pyplot as plt
from sort import sort_nicely
# from multiprocessing import Process, Manager
# import pickle
import json

## Get datase
base_dir = '/home/datasets/GAIT-IT'
metadata_dir = '/home/datasets/metadata'

sample_count = 0
# all_images = {'train': [], 'validation': [], 'test': []}
# all_labels = {'train': [], 'validation': [], 'test': []}
# subjects_data = {}
# train_subjs = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','s15','s16','s17','s18','s19']
# validation_subjs = ['s20','s21']
# test_subjs = ['s22','s23']
# train_images = []; train_labels = []
# validation_images = []; validation_labels = []
# test_images = []; test_labels = []

pat_dic = {'Diplegic' : 'pat1', 'Hemiplegic' : 'pat2', 'Neuropathic' : 'pat3', 'Normal' : 'normal', 'Parkinson' : 'pat4'}

classes = {'Diplegic' : 0, 'Hemiplegic' : 1, 'Neuropathic' : 2, 'Normal' : 3, 'Parkinson' : 4}
classes_inv = {0 : 'Diplegic', 1 : 'Hemiplegic', 2 : 'Neuropathic', 3 : 'Normal', 4 : 'Parkinson'}

## Train silhouettes directories

# Sort pathologies, OCD purposes only
pathologies = list(classes.keys())
sort_nicely(pathologies)
for pathology in pathologies:

    pathology_dir = base_dir + '/{}'.format(pathology)
    print(pathology_dir)
    pathology_subj_folders = [name for name in os.listdir(pathology_dir) if os.path.isdir(os.path.join(pathology_dir, name))]
    sort_nicely(pathology_subj_folders)
    
    # /Pathology/subj{i}/silhouettes/subj_{i}-pat_{j}-lvl_{k}-{l}_{direction}
    for subj_folder in pathology_subj_folders:

        if subj_folder not in ['s1']: continue
        # if subj_folder in train_subjs: subj_set = 'train'
        # elif subj_folder in validation_subjs: subj_set = 'validation'
        # elif subj_folder in test_subjs: subj_set = 'test'

        subj_folder_dir = os.path.join(pathology_dir, subj_folder)
        # print(subj_folder_dir)
        subj_silhouettes_dir = os.path.join(subj_folder_dir, 'silhouettes', 'side_view')
        # print(subj_silhouettes_dir)

        subj_silhouettes_folders = [name for name in os.listdir(subj_silhouettes_dir) if os.path.isdir(os.path.join(subj_silhouettes_dir, name))]
        sort_nicely(subj_silhouettes_folders)

        folders = [f for f in subj_silhouettes_folders if '_' in f]
        for folder in folders:

            # Initialize dictionary to store key frames
            key_frames = {}

            # Directory with metadata about current folder
            subj_silhouettes_metadata_dir = subj_silhouettes_dir.replace('GAIT-IT', 'metadata')
            subj_pat_metadata = os.path.join(subj_silhouettes_metadata_dir,'metadata/key_frames.json')

            with open(subj_pat_metadata) as f:
                key_frames = json.load(f)

            # Directory with the sillouettes images
            subj_pat_lvl_dir = os.path.join(subj_silhouettes_dir, folder)
            # print(subj_pat_lvl_dir)

            files = os.listdir(subj_pat_lvl_dir)
            sort_nicely(files)
            file_names = [files[f] for f in key_frames[folder]]
            
            pose_dir = subj_silhouettes_dir.replace('silhouettes','pose')

            if 'lvl1' in folder:
                pose_lvl_dir = os.path.join(pose_dir,subj_folder + pat_dic[pathology] + 'lvl1')
            elif 'lvl2' in folder:
                pose_lvl_dir = os.path.join(pose_dir,subj_folder + pat_dic[pathology] + 'lvl2')
            elif 'normal' in folder:
                pose_lvl_dir = os.path.join(pose_dir,subj_folder + pat_dic[pathology])

            pose_files = os.listdir(pose_lvl_dir)
            sort_nicely(pose_files)

            # Convert images to numpy arrays, put in batches
            # for file_name in file_names:
            for i in range(0, len(file_names)-8, 9):
                for j in range(0,9):
                    file_path = os.path.join(subj_pat_lvl_dir, file_names[i+j])

                    file_number = file_names[i+j].replace('frame','')
                    file_number = int(file_number.replace('.jpg',''))

                    print(file_number)
                    print(pose_files[file_number])
#                     img = image.load_img(file_path, target_size=(224, 224))
#                     img_tensor = image.img_to_array(img)
#                     sample_count += 1

#                     all_images[subj_set].append(img_tensor)
#                     all_labels[subj_set].append(classes[pathology])
# print(len(all_images['train'])); print(len(all_images['validation'])); print(len(all_images['test']))
# print(len(all_labels['train'])); print(len(all_labels['validation'])); print(len(all_labels['test']))
                