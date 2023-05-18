import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
img = cv2.imreadimage = cv2.imread('../car//image/someshapes.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply bilateral filtering to reduce noise while preserving edges
blur = cv2.bilateralFilter(gray, 11, 17, 17)
# Detect edges using Canny edge detector
edges = cv2.Canny(blur, 30, 200)
np.set_printoptions(threshold=sys.maxsize)
cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.imwrite('edges.jpg', edges)

e_img = cv2.imread('edges.jpg', 0)
# print(e_img)
print(e_img.shape)
arr = np.array2string(e_img, separator=', ')
print(arr)

with open("output.txt", "w") as txt_file:
    for line in arr:
        txt_file.write(str(line))


np.savetxt('npfile', e_img, delimiter=',', fmt='% 4d')