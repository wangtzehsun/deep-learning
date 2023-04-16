from keras.datasets import mnist
from keras.utils import np_utils
# import os;
# print(os.getcwd())
(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()
# print(x_train_image.shape)
x_Train = x_train_image.reshape(len(x_train_image), 28, 28, 1).astype('float32')
x_Train_normalize = x_Train / 255
y_Train_OneHot = np_utils.to_categorical(y_train_label)

x_Test = x_test_image.reshape(len(x_test_image), 28, 28, 1).astype('float32');
x_Test_normalize = x_Test / 255
y_Test_OneHot = np_utils.to_categorical(y_test_label)

# CNN
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
model = Sequential()
model.add(Conv2D(filters=16, kernel_size=(5,5), padding='same', input_shape=(28,28,1), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(filters=36, kernel_size=(5,5), padding='same', activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dropout(0.25))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
print(model.summary())

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=x_Train_normalize, y=y_Train_OneHot, validation_split=0.3, epochs=5, batch_size=100, verbose=2)
score = model.evaluate(x_Test_normalize, y_Test_OneHot)
print('accuracy:' + str(score[1]))