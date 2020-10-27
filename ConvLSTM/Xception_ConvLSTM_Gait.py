####### Imports #######
import re
import os
import sys
sys.path.append('/home/pfa/Documents/PathologicalGaitClassification')
import numpy as np
from keras.applications import Xception
from keras.models import Model
from keras.layers import Dense, Input, ConvLSTM2D, GlobalAveragePooling2D, Dropout
from keras.layers.wrappers import TimeDistributed
from keras.optimizers import Nadam
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.preprocessing import image
from keras.utils import to_categorical
import matplotlib.pyplot as plt
from sort import sort_nicely
from multiprocessing import Process, Manager
import pickle
import json

########### Get datase
base_dir = '/home/datasets/GAIT-IT'
metadata_dir = '/home/datasets/metadata'

sample_count = 0
all_images = []
all_labels = []
# subjects_data = {'train': {}, 'validation': {}, 'test': {}}
subjects_data = {}
# train_subjs = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10']
# validation_subjs = ['s11','s12']
# test_subjs = ['s13','s14']
train_images = []; train_labels = []
validation_images = []; validation_labels = []
test_images = []; test_labels = []

classes = {'Diplegic' : 0, 'Hemiplegic' : 1, 'Neuropathic' : 2, 'Normal' : 3, 'Parkinson' : 4}
classes_inv = {0 : 'Diplegic', 1 : 'Hemiplegic', 2 : 'Neuropathic', 3 : 'Normal', 4 : 'Parkinson'}

########### Train silhouettes directories

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

        if subj_folder not in ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14']: continue

        # if subj_folder in train_subjs: subj_set = 'train'
        # elif subj_folder in validation_subjs: subj_set = 'validation'
        # elif subj_folder in test_subjs: subj_set = 'test'


        subj_folder_dir = os.path.join(pathology_dir, subj_folder)
        # print(subj_folder_dir)
        subj_silhouettes_dir = os.path.join(subj_folder_dir, 'silhouettes', 'side_view')
        # print(subj_silhouettes_dir)

        subj_silhouettes_folders = [name for name in os.listdir(subj_silhouettes_dir) if os.path.isdir(os.path.join(subj_silhouettes_dir, name))]
        sort_nicely(subj_silhouettes_folders)

        if subj_folder not in subjects_data: subjects_data[subj_folder] = {}
        subjects_data[subj_folder][pathology] = {}
        subjects_data[subj_folder][pathology]["images"] = []
        subjects_data[subj_folder][pathology]["labels"] = []

        folders = [f for f in subj_silhouettes_folders if '_' in f]
        for folder in folders:

            # Initialize dictionary to store key frames
            key_frames = {}

            # Directory with metadata about current folder
            subj_silhouettes_metadata_dir = subj_silhouettes_dir.replace('GAIT-IT-2_silhouettes2', 'metadata')
            subj_pat_metadata = os.path.join(subj_silhouettes_metadata_dir,'metadata/key_frames.json')

            with open(subj_pat_metadata) as f:
                key_frames = json.load(f)

            # Directory with the sillouettes images
            subj_pat_lvl_dir = os.path.join(subj_silhouettes_dir, folder)
            # print(subj_pat_lvl_dir)

            files = os.listdir(subj_pat_lvl_dir)
            sort_nicely(files)
            file_names = [files[f] for f in key_frames[folder]]
            
            # Convert images to numpy arrays, put in batches
            # for file_name in file_names:
            for i in range(0, len(file_names), 9):

                img_tensors = []
                for j in range(0,9):
                    file_path = os.path.join(subj_pat_lvl_dir, file_names[i+j])
                    img = image.load_img(file_path, target_size=(224, 224))
                    img_tensor = image.img_to_array(img)
                    img_tensors.append(img_tensor)
                    sample_count += 1
                
                img_tensor_5D = np.stack(img_tensors)
                
                subjects_data[subj_folder][pathology]["images"].append(img_tensor_5D)
                subjects_data[subj_folder][pathology]["labels"].append(classes[pathology])

def split_data(subjects_data, val_subs, test_subs):

    # # Determine K-folds cross validation subject
    # validation_subject = 'sub{}'.format(foldIteration)
    # print(validation_subject)

    # Create training and validation inputs and labels lists
    train_images = []; train_labels = []
    validation_images = []; validation_labels = []
    test_images = []; test_labels = []

    # Iterate through subjects data to fill training and validation sets
    for subject in subjects_data:
        for pathology in subjects_data[subject]:
            if subject in val_subs:
                validation_images.extend(subjects_data[subject][pathology]["images"])
                validation_labels.extend(subjects_data[subject][pathology]["labels"])
            elif subject in test_subs:
                test_images.extend(subjects_data[subject][pathology]["images"])
                test_labels.extend(subjects_data[subject][pathology]["labels"])
            else:
                train_images.extend(subjects_data[subject][pathology]["images"])
                train_labels.extend(subjects_data[subject][pathology]["labels"])

    # Convert data lists to arrays
    train_images = np.array(train_images)
    train_labels = np.array(train_labels)
    train_labels = to_categorical(train_labels)
    train = {}
    train["images"] = train_images
    train["labels"] = train_labels

    validation_images = np.array(validation_images)
    validation_labels = np.array(validation_labels)
    validation_labels = to_categorical(validation_labels)
    validation = {}
    validation["images"] = validation_images
    validation["labels"] = validation_labels

    # Check if test set was defined
    try:
        test_images = np.array(test_images)
        test_labels = np.array(test_labels)
        test_labels = to_categorical(test_labels)
        test = {}
        test["images"] = test_images
        test["labels"] = test_labels
    except ValueError:
        print("Test set is empty")
        test = {}
        test["images"] = test_images
        test["labels"] = test_labels

    # Print total sample count and training and validation set counts
    print("Total samples: ", sample_count)
    print(len(train_images))
    print(len(validation_images))
    print(len(test_images))

    return train, validation, test


img_height = 224
img_width = 224
no_of_frames = 9
channels = 3
no_of_epochs = 50
batch_size_value = 5

input_video = Input(shape=(no_of_frames, img_width, img_height, channels))
cnn_base = Xception(input_shape=(img_width, img_height, channels), weights="imagenet", include_top=False)
cnn_base.trainable = False

encoded_frames = TimeDistributed(cnn_base)(input_video)
encoded_sequence = ConvLSTM2D(64, kernel_size=(7, 7), strides=(2, 2),padding='same', return_sequences=False)(encoded_frames)

GAP_layer = GlobalAveragePooling2D()(encoded_sequence)

hidden_layer_1 = Dense(activation="relu", units=1024)(GAP_layer)
drop_layer=Dropout(0.2)(hidden_layer_1)
hidden_layer_2 = Dense(activation="relu", units=512)(drop_layer)
outputs = Dense(5, activation="softmax")(hidden_layer_2)
model = Model([input_video], outputs)

model.summary()
nadam_optimizer = Nadam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, schedule_decay=0.004)

model.compile(loss="categorical_crossentropy", optimizer=nadam_optimizer, metrics=["accuracy"])

# serialize model to JSON
model_json = model.to_json()
with open("Xception_convLSTM2D_model.json", "w") as json_file:
    json_file.write(model_json)

# Save the model according to the conditions
checkpoint = ModelCheckpoint("Xception_convLSTM2D.h5", monitor='val_acc', verbose=1, save_best_only=True,
                            save_weights_only=False,
                            mode='auto', period=1)
early_stopping_criteria = EarlyStopping(monitor='val_acc', min_delta=0, patience=20, verbose=1, mode='auto')

# Split data into training, validation and test sets
# train, validation, test = split_data(subjects_data=subjects_data, foldIteration=k, test_sub=None)
train, validation, test = split_data(subjects_data=subjects_data, val_subs=['s11','s12'] , test_subs=['s13','s14'])
train_images = train["images"]; train_labels = train["labels"]
validation_images = validation["images"]; validation_labels = validation["labels"]
test_images = test["images"]; test_labels = test["labels"]

history = model.fit(
        train_images, train_labels,
        validation_data=(validation_images, validation_labels),
        verbose=1,
        epochs=no_of_epochs,
        callbacks=[checkpoint, early_stopping_criteria])


# prediction = model.evaluate_generator(test_set)
# print("Loss: ", prediction[0], "Accuracy: ", prediction[1])

# Plot training & validation accuracy values
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'], loc='upper left')
plt.show()
