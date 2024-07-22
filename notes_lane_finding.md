# **Lane Finding Notes**

## Lesson 1: Basics
- Loading an image (multidimensional numpy array, containing rel intensities of each pixel)

## Lesson 2: Grayscale Conversion
- Always make a copy of a varible
- Convert to grayscale using inbuilt opencv function ` COLOR_RGB2GRAY `
  
## Lesson 3: Gaussain Blur
- Smoothening our image and reducing noise.
- Gaussing blur applies avg value of intesity of neighbouring pixels to the pixel
- A kernel of 5x5 and a deviation of 0

## Lesson 4: Canny Edge Detection
- The image can be represented in x and y ie. as a function of x and y
- Canny performs derivative of f(x,y) and finds the gradient
- the gradients which lie in the range are only accepted and generlly the ratio of thresholds are 1:2 or 1:3
- The one with the stepest gradient, that is the intensity change , is turned to white

## Lesson 5:Region of interest
- We are only interested in a region , i.e the road
- we defined a function `region_of_interest` in which a traingular part of road in highlighted using `numpy array` ,`zeros_like` _(mask)_,`fillpoly`_(fills the mask0)_

## Lesson 6: Using Bitwise operator
- Binary Representation:
1. 0 = 0 = black
2. 255= 11111111  =white
- Taking **AND** operator with 0 and any number results into 0 , ie black with any pixel results in black
- Whereas taking with a white results in the same pixel value , therefore only the white lines present in masked triangle remains.

## Lesson 7: Hough Transformation
- A single point in xy plane when converted in hough space , we get a line . In simplier words for a family of lines passing through a point in xy coordinate plane , when ploted in m vs b , we get a line .
- When we plot more than 1 nmber of points in Hough space we get a number of intersections in H-plane , then we divide into bins and the bin with the most intersection is selected (the values of m and b) . The line obtained fits the best.
- The same thing is carried for p = xcostheta + y sintheata
- Here we get Sinosoidual curve and the values of p and theta

## Lesson 8: Displaying the lines
- `cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)` here 2 = rho , theta=1deg , 100 = threshold value
- Then we created a black image using `zeros_like`
- The lines give us a 3d array which needs to be converted into 2d using `reshape`
- Then drew a line using `cv2.line` on black image and then added it with the original image
- _Note: We can even skip the black image part_

## Lesson 9: Averaging the line
- `polyfit` converts the coordinates into a polynomial of degree 1 , and returns a vector
- Then we find the average value of all slopes and intercepts
- axis = 0 helps to go below a column
- Then we assign the point from where the line should start and also finds the corresponding x coordinate using the values of slope and intercept (average)
- Then we get a single average line

## Lesson 10: Video
- We modified the code a little , to make it compactible with video _(frame by frame)_
