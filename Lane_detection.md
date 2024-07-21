# LANE DETECTION IN IMAGE AND VIDEO USING OPEN CV

## First import important libraries like cv2 and numpy

## STEPS FOR LANE DETECTION
1. GET THE CANNY EDGES IN THE IMAGE -> THIS IS IMPORTANT SO WE CAN MAINLY FOCUS ON THE EDGES OF THE ROAD AND LANE SYMBOLS IN THE IMAGE AND IGNORE ALL OTHER NOISES 
    - Step 1 is to convert the image to grayscale as dealing with one colour channel in grayscale is more easy as compared to three channels in bgr/rgb image and it makes edge detection more easy
    - Step 2 is to apply gaussian Blur to the image to get rid of the useless noise and extra edges in the image while edge detection like the sky,trees etc. This is done using a 5*5 kernel.
    - Step 3 is to apply the canny edge function and get the image with only edges shown in it. Edge detection is done based on the gradient i.e. change in color intensity in the x or y direction between adjacent pixel, its two arguements are threshold1 and threshold2, any gradient change above threshold2 is accepted and made white (counted as edge), any gradient below threshold1 is discarded and any gradient between threshold1 and threshold 2 is only accepted if it is adjacent to a strong gradient.

2. GET THE REGION OF INTEREST i.e. ONLY THE REGION OF IMAGE CONTAINING THE LANE WHICH WE WANT TO DETECT AND FOLLOW
    - We first use matplotlib to display the image produced after canny edge and get the rough idea about the cordinates of the polygon having ROI
    - Then we create a blank image called mask having same dimensions as original image and draw the polygon with white colour on the mask
    - Then we perform bitwise and operation between the canny edge image and the mask so we get an image only having ROI shown as lane edges

3. FROM THE ROI GENERATED IN STEP 2 WE DRAW HOUGH LINES ON THE EDGES SHOWN IN THE ROI
    - HOUGH LINES FUNCTION TAKES THE FOLLOWING THINGS AS PARAMETERS:
        - Image on which hough lines has to be drawn, the roi image in our case
        - Value of rho, i.e. distance resolution of accumulator pixels i.e. Y axis in the hough space in unit pixels
        - Value of theta i.e. degree resolution of accumulator pixels in unit : radian
        - theta and rho values specify the dimension of each bin in hough space, smaller the bins, greater the accuracy, but they should not be much smaller too.
        - Then comes the threshold value i.e. minimum  number of votes ie.e intersection in bin to make the bin an accepted candidate so values of that bin can be used.
        - Then comes the placeholder array that is generally passed as an empty array.
        - Then comes the minimum length of the line req for a line to be an accepted candidate.
        Then comes the maximum gap length between two lines i.e. lines having gap of this value or less can be merged.
    - This hough line function return a 2D array of size n * 4 where n is the num of lines and each line is a array of 4 integers i.e. x1,y1 and x2,y2.

4. FIND THE PARAMETER (M AND B) FOR ALL LINES (Y = MX + B) PRODUCED BY THE HOUGH SPACE AND AVERAGE OUT THE VALUES TO GET A SINGLE LINE FOR CONVENIENCE
    - Create list for m and b the left line and the right line seperately
    - iterate through each elemnent in the lines 2D array i.e. cordinates of each line and using the POLYFIT function find the values of m and b for that set of points by passing the two points and degree of polynomial (in our case 1 i.e. y = mx + c) to be obtained.
        - Using the image display in matplotlib we found out that the left line has a neg slope by looking at change in x and y and right line hasc a positive slope.
    - now we append the respective values of m and b as a tuple to respective left or right lines' list.
    - we then find avg values of m and b for each left and right line and then using 'cv.line' we draw these lines with avg m and b on a new masked image produced of same size as original image.

5. FINAL STEP IS TO ADD THE MAIN IMAGE OF ROAD AND THE MASKED IMAGE WITH THE LINES DRAWN IN THE LAST STEP BY USING 'cv.addWeighted' by giving 0.6 to 0.8 weight to main image and weight 1 to 1.2 to the masked image.


## WE CAN USE THIS PROCEDURE FOR AN IMAGE AND IN CASE OF VIDEOS WE CAN APPLY THIS PROCEDURE WHILE READING EACH INDIVIDUAL FRAME OF THE VIDEO IN THE WHILE LOOP SO WE CAN GET A CONTINUOS EFFECT OF THE LANE DETECTION METHOD IN THE VIDEO.

## LINK FOR REF
[Lane detection using OpenCV](https://www.youtube.com/watch?v=eLTLtUVuuy4 "LCO")


