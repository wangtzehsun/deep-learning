from PIL import Image
img = Image.open('3.png')
print(img)
# reImg = img.resize((28,28))
# print(reImg)

import numpy as np
# image to 2d array use numpy -> reImg.convert("L") to gray
# img1 28 * 28 gray image
# img1 = np.array(reImg.convert('L'))

# import matplotlib.pyplot as plt
# plt.imshow(img1, cmap=plt.get_cmap('gray'))
# plt.show()
#
# img1 = img1.reshape(1, (28*28))
# img1 = img1.astype('float32') / 255
#
# from keras.models import load_model
# model = load_model('model1.h5')
# predicted_ans = model.predict(img1)
# print(predicted_ans)
# # predicted_ans = model.predict_classes(img1)
# predicted_ans = np.argmax(model.predict(img1), axis=-1)
# print('predicted result: ', str(predicted_ans))