import cv2
from timeit import default_timer as timer
from collections import deque
import numpy as np

# original_image = cv2.imreadimage = cv2.imread('../../car//image/car1.jpg')
# original_image = cv2.imreadimage = cv2.imread('../../car//image/someshapes.jpg')
original_image = cv2.imreadimage = cv2.imread('../../car//image/someshapes2.jpg')

# Convert to grayscale
gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
# Apply bilateral filtering to reduce noise while preserving edges
blur = cv2.bilateralFilter(gray, 11, 17, 17)
# Detect edges using Canny edge detector
processed_image = cv2.Canny(blur, 30, 200)
cv2.imshow('processed_image', processed_image)
cv2.waitKey(0)

#=============================================================================================================

cols = processed_image.shape[0]
rows = processed_image.shape[1]
print(processed_image.shape)

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
for row in range(0, cols):
    for col in range(0, rows):
        if processed_image[row, col] == CONST_BLACK:
            processed_image[row, col] = CONST_BLACK_DONE
            q.append([row, col])
            bfs(processed_image, q)
end = timer()
print('bfs finish time: ', end - start)

sorted_top10_all_line_map = dict(sorted(contours_line_map.items(), key=lambda item: item[1], reverse=True)[1:11])
print('sorted_all_line_map', sorted_top10_all_line_map)

contours = []
for key in sorted_top10_all_line_map:
    contour = np.array(contours_line_arr[key])
    contours.append(contour)

def find_extremes(contour):
    min_x = rows
    max_x = 0
    min_y = cols
    max_y = 0

    for xy in contour:
        x = xy[0]
        y = xy[1]
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    extreme_arr = []

    max_y_for_min_x = 0
    min_y_for_min_x = cols
    max_y_for_max_x = 0
    min_y_for_max_x = cols
    max_x_for_max_y = 0
    min_x_for_max_y = rows
    max_x_for_min_y = 0
    min_x_for_min_y = rows

    CONST_MIN_XY_PIXEL_TOLERANCE = 1

    for xy in contour:
        x = xy[0]
        y = xy[1]
        if x>= min_x-CONST_MIN_XY_PIXEL_TOLERANCE and x <= min_x + CONST_MIN_XY_PIXEL_TOLERANCE:
            if y < min_y_for_min_x:
                min_y_for_min_x = y
            if y > max_y_for_min_x:
                max_y_for_min_x = y
        if x>= max_x-CONST_MIN_XY_PIXEL_TOLERANCE and x <= max_x + CONST_MIN_XY_PIXEL_TOLERANCE:
            if y < min_y_for_max_x:
                min_y_for_max_x = y
            if y > max_y_for_max_x:
                max_y_for_max_x = y
        if y>= min_y-CONST_MIN_XY_PIXEL_TOLERANCE and y <= min_y + CONST_MIN_XY_PIXEL_TOLERANCE:
            if x < min_x_for_min_y:
                min_x_for_min_y = x
            if x > max_x_for_min_y:
                max_x_for_min_y = x
        if y >= max_y - CONST_MIN_XY_PIXEL_TOLERANCE and y <= max_y + CONST_MIN_XY_PIXEL_TOLERANCE:
            if x < min_x_for_max_y:
                min_x_for_max_y = x
            if x > max_x_for_max_y:
                max_x_for_max_y = x

    corners = [[min_x, min_y_for_min_x], [min_x, max_y_for_min_x],
               [max_x, min_y_for_max_x], [max_x, max_y_for_max_x],
               [min_x_for_min_y, min_y], [max_x_for_min_y, min_y],
               [min_x_for_max_y, max_y], [max_x_for_max_y, max_y]]
    a=sorted(contour, key=lambda x: (x[0], x[1]))
    CONST_PIXEL_TOLERANCE = 30

    for i in range(len(corners)):
        for j in range(i+1, len(corners)):
            delta_x = corners[i][0] - corners[j][0]
            delta_y = corners[i][1] - corners[j][1]
            if (delta_x <= CONST_PIXEL_TOLERANCE and delta_x >= 0-CONST_PIXEL_TOLERANCE) and (delta_y <= CONST_PIXEL_TOLERANCE and delta_y >= 0-CONST_PIXEL_TOLERANCE):
                corners[i] = [-1,-1]
                break

    extremes = [subarray for subarray in corners if subarray != [-1, -1]]
    return extremes

for contour in contours:
    extremes = find_extremes(contour)
    print('extremes', extremes)
    for abc in extremes:
        cv2.circle(original_image, (abc[0], abc[1]), 10, (0, 0, 255), -1)
    cv2.imshow('Contours', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()