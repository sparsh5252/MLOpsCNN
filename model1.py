from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense , Dropout , BatchNormalization
from keras.models import Sequential
 
no_of_epochs = 1
k_size = 3
p_size = (2,2)

model = Sequential()

model.add(Convolution2D(filters=32,kernel_size=(k_size,k_size),activation='relu',input_shape=(64, 64, 3)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size= p_size))
model.add(Dropout(0.25))


model.add(Convolution2D(filters=64,kernel_size=(k_size,k_size),activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size= p_size))
model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(units=256, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.25))

model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

from keras_preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(
        '/root/cat_dog_data/train/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        '/root/cat_dog_data/test/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

model.fit_generator(
        training_set,
        steps_per_epoch=1000,
        epochs=no_of_epochs,
        validation_data=test_set,
        validation_steps=250)

