import cv2 as cv
import numpy as np

def canny(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    canny = cv.Canny(blur, 50, 150)
    return canny

def ROI(image):
    h = image.shape[0]
    triangle = np.array([(200, h), (1100, h), (550, 250)])
    mask = np.zeros_like(image)
    poly = cv.fillPoly(mask, [triangle], 255)
    roi = cv.bitwise_and(image, poly)
    return roi

def produce_lines(image):
    c = canny(image)
    r = ROI(c)
    lines = cv.HoughLinesP(r, 2, np.pi/180, 100, np.array([]), 40, 5)
    return lines

def make_coordinates(image, parameters):
    slope, intercept = parameters
    y1 = image.shape[0]
    y2 = int((3 / 5) * y1)
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return (x1, y1), (x2, y2)

def avg_slope_intercept_lines(image, lines):
    left = []
    right = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            param = np.polyfit((x1, x2), (y1, y2), 1)
            slope = param[0]
            intercept = param[1]
            if slope < 0:
                left.append((slope, intercept))
            else:
                right.append((slope, intercept))
    
    if left:
        left_avg = np.average(left, axis=0)
        left_line = make_coordinates(image, left_avg)
        cv.line(image, left_line[0], left_line[1], (255, 0, 0), 10)
    
    if right:
        right_avg = np.average(right, axis=0)
        right_line = make_coordinates(image, right_avg)
        cv.line(image, right_line[0], right_line[1], (255, 0, 0), 10)
    
    return image

def display_lane_lines(image):
    lines = produce_lines(image)
    mask = np.zeros_like(image)
    lane = avg_slope_intercept_lines(mask, lines)
    return cv.addWeighted(image, 0.8, lane, 1, 1)


#road image
# img = cv.imread('road.jpg')
# lane = np.copy(img)
# l = display_lane_lines(img)
# cv.imshow('lane', l)
# cv.waitKey(0)
# cv.destroyAllWindows()


#road video
cap = cv.VideoCapture('road_vid.mp4')
while(cap.isOpened):
    ret, frame = cap.read()
    
    if ret == True:
        lines = display_lane_lines(frame)
        cv.imshow('Road', lines)
        
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
