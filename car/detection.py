import cv2
img = cv2.imread('../../car//image/car4.jpg')
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply bilateral filtering to reduce noise while preserving edges
blur = cv2.bilateralFilter(gray, 11, 17, 17)

# Detect edges using Canny edge detector
edges = cv2.Canny(blur, 30, 200)

# Find contours in the edged image

contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area in descending order
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# Loop over the contours
for c in contours:
    # Approximate the contour with a polygon
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)

    # If the polygon has 4 vertices, it may be a license plate
    if len(approx) == 4:
        # Draw the contour and show the image
        cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
        cv2.imshow("License Plate Detection", img)
        cv2.waitKey(0)
        break

cv2.destroyAllWindows()
