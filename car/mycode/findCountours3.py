import cv2
from timeit import default_timer as timer
from collections import deque
import numpy as np

original_image = cv2.imreadimage = cv2.imread('../../car//image/car1.jpg')
# original_image = cv2.imreadimage = cv2.imread('../../car//image/someshapes.jpg')
# original_image = cv2.imreadimage = cv2.imread('../../car//image/someshapes2.jpg')

# Convert to grayscale
gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
# Apply bilateral filtering to reduce noise while preserving edges
blur = cv2.bilateralFilter(gray, 11, 17, 17)
# Detect edges using Canny edge detector
processed_image = cv2.Canny(blur, 30, 200)
cv2.imshow('processed_image', processed_image)
cv2.waitKey(0)

#=============================================================================================================

rows = processed_image.shape[0]
cols = processed_image.shape[1]

#CONSTANT VARIABLE
CONST_BLACK = 0
CONST_BLACK_DONE = 2
CONST_WHITE = 255

q = deque()
contours_line_arr = []
contours_line_map = {}
count_area = 0


def bfs(processed_image, q):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    contour_line = []
    count_area = 0
    while (len(q) > 0):
        curr = q.popleft()
        is_outer_line_flag  = False

        for dir in dirs:
            i = curr[0] + dir[0]
            j = curr[1] + dir[1]
            if (isBlack(processed_image, i, j)):
                if processed_image[i][j] != CONST_BLACK_DONE:
                    q.append([i, j])
                    processed_image[i][j] = CONST_BLACK_DONE
                continue
            is_outer_line_flag = True

        if is_outer_line_flag:
            contour_line.append([curr[1], curr[0]])
        else:
            count_area += 1

    contours_line_map[len(contours_line_arr)] = count_area
    contours_line_arr.append(contour_line)


#isBlack true may contain either black done or black
def isBlack(processed_image, i, j):
    return i >= 0 and i < len(processed_image) and j >= 0 and j < len(processed_image[0]) and processed_image[i][j] != CONST_WHITE


start = timer()
for row in range(0, rows):
    for col in range(0, cols):
        if processed_image[row, col] == CONST_BLACK:
            processed_image[row, col] = CONST_BLACK_DONE
            q.append([row, col])
            bfs(processed_image, q)
end = timer()
print('bfs finish time: ', end - start)

sorted_top10_all_line_map = dict(sorted(contours_line_map.items(), key=lambda item: item[1], reverse=True)[0:11])


contours_sorted_by_x = []
for key in sorted_top10_all_line_map:
    contour = np.array(contours_line_arr[key])
    contours_sorted_by_x.append(sorted(contour, key=lambda x: (x[0], x[1])))


x = 0
diff_x = []
for contour in contours_sorted_by_x:
    y_min = 0
    y_max = 0
    diff_arr_x = []
    for xy in contour:
        if xy[0] != x:
            diff_arr_x.append(y_max - y_min)
            x = xy[0]
            y_min = xy[1]
        else:
            y_max = xy[1]
    diff_x.append(diff_arr_x)

y = 0
diff_y = []
for contour in contours_sorted_by_x:
    x_min = 0
    x_max = 0
    diff_arr_y = []
    contour = sorted(contour, key=lambda x: (x[1], x[0]))
    for xy in contour:
        if xy[1] != y:
            diff_arr_y.append(x_max - x_min)
            y = xy[1]
            x_min = xy[0]
        else:
            x_max = xy[0]
    diff_y.append(diff_arr_y)


# input = [0,3,6,9,12,12,12,12,12,12,12,12,9,6,3,0]
# result = [3,3,3,3,0,0,0,0,0,0,0,-3,-3,-3,-3]
# # result = list(map(lambda x, y: y - x, input[:-1], input[1:]))
# result = list(map(lambda x, y: y - x, diff_x[0][:-1], diff_x[0][1:]))
# print(result)

rectangle_contours = []


def add_rectangle_contours(diff_x, diff_y):
    is_rectangle_flag = False
    for i in range(len(diff_x)):
        diff_x_arithmetic = list(map(lambda x, y: y - x, diff_x[i][:-1], diff_x[i][1:]))
        diff_y_arithmetic = list(map(lambda x, y: y - x, diff_y[i][:-1], diff_y[i][1:]))
        is_rectangle_flag = diff_x_arithmetic.count(0) / len(diff_x_arithmetic) > 0.9
        is_rectangle_flag = (diff_y_arithmetic.count(0) / len(diff_y_arithmetic) > 0.8) and is_rectangle_flag
        if is_rectangle_flag:
            rectangle_contours.append(contours_sorted_by_x[i])


add_rectangle_contours(diff_x, diff_y)

rectangle_contours = np.array(np.concatenate(rectangle_contours))
for contour in rectangle_contours:
    cv2.circle(original_image, (contour[0], contour[1]), 1, (0, 0, 255), -1)
cv2.imshow('Contours', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()