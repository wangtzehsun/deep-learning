import cv2

image = cv2.imread('../../car//image/car1.jpg')
cv2.imshow('Original', image)
cv2.waitKey()

#traditional way of GrayScaling
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("GrayScale", gray_image)
# cv2.waitKey()
# cv2.destroyAllWindows()

# faster way of GrayScaling
fast_gray_img = cv2.imread('../../car//image/car1.jpg', 0)
cv2.imshow("fast_gray_img", fast_gray_img)
cv2.waitKey()
cv2.destroyAllWindows()


