from keras.applications import Xception
from keras.models import Model
from keras.layers import Dense, Input, ConvLSTM2D, GlobalAveragePooling2D, Dropout, np
from keras.layers.wrappers import TimeDistributed
from keras.optimizers import Nadam
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras_video import VideoFrameGenerator
import keras
import matplotlib.pyplot as plt

# use sub directories names as classes
class_ids = ['neg', 'pos']

# pattern to get videos and classes
video_path = '/home/vislab/Downloads/Videos/Videos/fire_videos/{classname}/*.avi'

img_height = 299
img_width = 299
no_of_frames = 15#21
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
outputs = Dense(2, activation="softmax")(hidden_layer_2)
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

# for data augmentation
data_augmentation = keras.preprocessing.image.ImageDataGenerator(
    zoom_range=.1,
    rotation_range=8,
    width_shift_range=.2,
    height_shift_range=.2)

# Create video frame generator
train_set = VideoFrameGenerator(
    classes=class_ids,
    glob_pattern=video_path,
    nb_frames=no_of_frames,
    split_test=.4,
    split_val=.2,
    shuffle=True,
    batch_size=batch_size_value,
    target_shape=(img_width, img_height),
    nb_channel=channels,
    transformation=data_augmentation,
    use_frame_cache=True)

validation_set = train_set.get_validation_generator()

test_set = train_set.get_test_generator()

history = model.fit_generator(
        train_set,
        validation_data=validation_set,
        verbose=1,
        epochs=no_of_epochs,
        callbacks=[checkpoint, early_stopping_criteria])

prediction = model.evaluate_generator(test_set)
print("Loss: ", prediction[0], "Accuracy: ", prediction[1])

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
