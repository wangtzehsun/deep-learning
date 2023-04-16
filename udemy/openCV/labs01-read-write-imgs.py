import cv2

image = cv2.imread('../../car//image/car1.jpg')
cv2.imshow('MyTitle', image)
cv2.waitKey()
cv2.destroyAllWindows()

#(height, width, rgb values)
print(image.shape)
# Let's print each dimension of the image
print('Height of Image:', int(image.shape[0]), 'pixels')
print('Width of Image: ', int(image.shape[1]), 'pixels')

#save image
cv2.imwrite('test.jpg', image)
cv2.imwrite('test.png', image)