import cv2
import numpy as np

# Let's load a simple image with 3 black squares
image = cv2.imread('../../car//image/shapes_donut.jpg')
cv2.imshow('Input Image', image)

# Grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Canny Edges', edged)

# Finding Contours
# Use a copy of your image e.g. edged.copy(), since findContours alters the image
# Find contours in the edged image
# Approximation Methods
# Using cv2.CHAIN_APPROX_NONE stores all the boundary points. But we don't necessarily need all bounding points. If the points form a straight line, we only need the start and ending points of that line.
# Using cv2.CHAIN_APPROX_SIMPLE instead only provides these start and end points of bounding contours, thus resulting in much more efficent storage of contour information..
# contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#retrieve mode : cv2.RETR_EXTERNAL, cv2.RETR_LIST, cv2.RETR_TREE
contours, hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Edges After Contouring', edged)

print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# Use '-1' as the 3rd parameter to draw all
cv2.drawContours(image, contours, -1, (0,255,0), 3)
print(contours)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()