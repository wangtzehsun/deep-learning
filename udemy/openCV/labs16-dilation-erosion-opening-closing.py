import cv2
import numpy as np

image = cv2.imread('../../car//image/opencv.png', 0)
# image = cv2.imread('../../car//image/car1.jpg', 0)
cv2.imshow('Original', image)

# Let's define our kernel size
kernel = np.ones((5,5), np.uint8)

# Now we erode
erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow('Erosion', erosion)

#
dilation = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow('Dilation', dilation)

# Opening - Good for removing noise
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)

# Closing - Good for removing noise
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)
cv2.waitKey(0)


cv2.destroyAllWindows()