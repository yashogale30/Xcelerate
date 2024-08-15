import cv2
import numpy as np

def canny(image):
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #kernel of 5x5
    canny = cv2.Canny(blur , 50 , 150 )
    #ratio of 1:3
    return canny

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([[(200,height),(1100,height),(550,250)]])
    mask = np.zeros_like(image)
    #black image
    cv2.fillPoly(mask,polygons,255)
    #fills the region of interest with white
    masked_image = cv2.bitwise_and(mask,image)
    #combining two images
    return masked_image

def display_lines(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None:
        for x1,y1,x2,y2  in lines:
            #drawing lines
            cv2.line(line_image,(x1,y1),(x2,y2),(0,255,0),10)
    return line_image

def average_slope_intercept(image,lines):
    left_fit =[]
    right_fit=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        
        parameters=np.polyfit((x1,x2),(y1,y2),1)
        #convert into polynomial of dgree 1 
        slope=parameters[0]
        intercept=parameters[1]
        
        if slope <0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))

    left_fit_average = np.average(left_fit,axis=0)
    right_fit_average=np.average(right_fit,axis=0)
    left_line=make_coorinates(image,left_fit_average)
    right_line=make_coorinates(image,right_fit_average)
    return np.array([left_line,right_line])

def make_coorinates(image,lineparameter):
    #takes the c & m & y finds x
    slope,intercept=lineparameter
    y1 = image.shape[0]
    y2 = int(y1*(3/5))

    x1= int((y1 - intercept)/slope)
    x2= int((y2 - intercept)/slope)
    return np.array([x1,y1,x2,y2]) 



 
#importing the image
image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
#using canny method
canny_image = canny(lane_image)
cropped_image=region_of_interest(canny_image)
#implementing hough's plane
lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
#averaging the lines
averaged_lines=average_slope_intercept(lane_image,lines)
line_image = display_lines(lane_image,averaged_lines) 
# combined_image = cv2.bitwise_or(line_image,lane_image)     
combined_image=cv2.addWeighted(lane_image,0.8,line_image,1,1)            
cv2.imshow('result',combined_image)

cv2.waitKey(0)
cv2.destroyAllWindows

# cap =cv2.VideoCapture("test2.mp4")
# while(cap.isOpened()):
#     _, frame = cap.read()
#     canny_image = canny(frame)
#     cropped_image=region_of_interest(canny_image)
#     lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
#     averaged_lines=average_slope_intercept(frame,lines)
#     line_image = display_lines(frame,averaged_lines) 
#     # combined_image = cv2.bitwise_or(line_image,lane_image)     
#     combined_image=cv2.addWeighted(frame,0.8,line_image,1,1)            
#     cv2.imshow('result',combined_image)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
   

