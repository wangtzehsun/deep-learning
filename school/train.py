from keras.datasets import mnist
from keras.utils import np_utils
# import os;
# print(os.getcwd())
(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()
# print(x_train_image.shape)
x_Train = x_train_image.reshape(len(x_train_image), 784).astype('float32')
x_Train_normalize = x_Train / 255
y_Train_OneHot = np_utils.to_categorical(y_train_label)

x_Test = x_test_image.reshape(len(x_test_image), 784).astype('float32');
x_Test_normalize = x_Test / 255
y_Test_OneHot = np_utils.to_categorical(y_test_label)

from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(units=256, input_dim=784, kernel_initializer='normal', activation='relu'))
model.add(Dense(units=10, kernel_initializer='normal', activation='softmax'))
print(model.summary())

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=x_Train_normalize, y=y_Train_OneHot, validation_split=0.3, epochs=5, batch_size=100, verbose=2)
score = model.evaluate(x_Test_normalize, y_Test_OneHot)
print('accuracy:' + str(score[1]))

model.save('model1.h5')

print("saved===========")
