import cv2

image = cv2.imread('../../car//image/car1.jpg')

#print rgb values
B, G, R = image[10, 50]
print('B, G, R: ', B, G, R)
print(image.shape)

#gray image shape goes to 2d
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_img.shape)

#compare color image vs gray image
print(image[10, 50])
print(gray_img[10, 50])