import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from keras.models import load_model
import os

# dog_train_path = "C:/Users/user/pycharm/pythonProject/vataVisualizaion/dog_saved/"
# dog_train_file_dir = os.listdir(dog_train_path)
#
# x_train = []
# y_train = []
#
# for file in dog_train_file_dir:
#     img = Image.open(dog_train_path + file)
#     data = np.array(img)
#     x_train.append(data)
#     y_train.append(0)
#
# cat_train_path = "C:/Users/user/pycharm/pythonProject/vataVisualizaion/cat_saved/"
# cat_train_file_dir = os.listdir(cat_train_path)
#
# for file in cat_train_file_dir:
#     img = Image.open(cat_train_path + file)
#     data = np.array(img)
#     x_train.append(data)
#     y_train.append(1)
#     # print(file)
#     # print(data.shape)
#
# x_train = np.array(x_train)
# x_train_normalize = x_train.reshape(20, (100*100)).astype('float32')
# x_train_normalize = x_train_normalize / 255
# y_train_one_hot = np_utils.to_categorical(y_train)
# print(x_train_normalize[0])
# print(y_train_one_hot[0])
#
# model = Sequential();
# model.add(Dense(units=256, input_dim=(100*100), kernel_initializer='normal', activation='relu'))
# model.add(Dense(units=2, kernel_initializer='normal', activation='softmax'))
# # print(model.summary())
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x=x_train_normalize, y=y_train_one_hot, validation_split=0.2, epochs=100, batch_size=2, verbose=2)
# score = model.evaluate(x_train_normalize, y_train_one_hot)
# print('accuracy:' + str(score[1]))
# model.save('dogcat.h5')

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
img = Image.open('/school/cat_saved/2.jpg')
reImg = img.resize((100,100))
img1 = np.array(reImg.convert('L'))
plt.imshow(img1, cmap=plt.get_cmap('gray'))
plt.show()
img1 = img1.reshape(1, (100*100))
img1 = img1.astype('float32') / 255
model = load_model('dogcat.h5')
predicted_ans = np.argmax(model.predict(img1), axis=-1)
print('predicted result: ', str(predicted_ans))
