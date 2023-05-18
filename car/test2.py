import numpy as np
import cv2

array = np.load("F:/python-workspace/deep-learning/car/npfile")
cv2.imshow(array)
cv2.waitKey(0)