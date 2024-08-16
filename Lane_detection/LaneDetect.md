# CLASS LINE
#### Default constructor --> __init__(self, x1, y1, x2, y2) --> sets coordinates of a line and calculates slope and bias using funcs and stores them in self.slope and self.bias
1.  Compute_slope(self) --> Calculates slope of the line by gievn end coordinates.
2.  Compute_bias(self) --> Calculates the Y-coeff or bias of the gievn line by end coordinates.
3.  get_coords(self) --> returns a list of points [x1,y1,x2,y2] of a line.
4.  set_coords(self,x1,y1,x2,y2) --> sets coordinates of a line
5.  draw(self, img, color=[255, 0, 0], thickness=10) --> draws line of red colour on given image using cv2.line

---
---
---

# DETECTION OF LANE

1. region_of_interest(img, vertices) --> creates a mask image of size of image and sets colour of region of interest to white and as per the channel count of img i.e. 255 or (255,255) or (255,255,255). Then uses cv2.fillPolly function the mark the region of interest with the vertices on the black mask image and make the region of interest white as per colour channels of og image. Then perform bitwise and of the mask image with roi and og image and store in masked_image and return it. We will get an image having only roi and rest all black.

2. hough_lines_detection(img, rho, theta, threshold, min_line_len, max_line_gap) --> Here img is the output after canny transform. This func returns a list of size(n,4) where n is the number of lines detected in img and 4 means x1,y1,x2,y2.

3. weighted_img(img, initial_img, α=0.8, β=1., λ=0.) --> this func takes maked_img and og colour image as input and returns the weighted sum as calculated by (initial_img * α + img * β + λ).

4. compute_lane_from_candidates(line_candidates, img_shape) --> it takes input the list of lines produced by hough transform and shape of img on which hough transform was applied, stores them in two diff list for left and right lines depending on sign of slope and then takes median of slope and bias for left and right lines amd then sets coordinates for each left and right line as :
    - Coordinate Calculation for the Right Lane:

        x1, y1 = 0, lane_right_bias

        x1 = 0: This sets the x-coordinate of the starting point of the right lane line to 0. This is the left edge of the image.
        y1 = lane_right_bias: This sets the y-coordinate of the starting point to lane_right_bias, which is the y-intercept of the line, where the line crosses the y-axis.
        So, (0, lane_right_bias) is a point on the left side of the image where the right lane line starts.

        x2, y2 = np.int32(np.round((img_shape[0] - lane_right_bias) / lane_right_slope)), img_shape[0]

        y2 = img_shape[0]: This sets the y-coordinate of the second point to img_shape[0], which is the height of the image. This corresponds to the bottom of the image.
        x2 = np.int32(np.round((img_shape[0] - lane_right_bias) / lane_right_slope)): This calculates the x-coordinate of the second point by finding where the line intersects the bottom of the image. To do this:
        Subtract lane_right_bias from img_shape[0] to find the difference in height from the intercept to the bottom of the image.
        Divide this height difference by the slope (lane_right_slope) to get the corresponding x-coordinate where the line would intersect the bottom of the image.
        Use np.round to round the value to the nearest integer, and np.int32 to ensure it's an integer suitable for image processing.
        So, np.int32(np.round((img_shape[0] - lane_right_bias) / lane_right_slope)), img_shape[0] is a point on the bottom of the image where the right lane line would intersect.

        Purpose
        Defining the Line Segment: These calculations define a line segment representing the right lane boundary. By specifying the starting and ending coordinates of the line segment, the code ensures that the line covers the portion of the image where the lane is expected to appear.
        Image Coordinate System: The image coordinate system has the origin (0, 0) at the top-left corner, with x increasing to the right and y increasing downward. The calculations ensure that the line spans from the top to the bottom of the image.
        Visualization
        Starting Point: (0, lane_right_bias) is on the left side of the image at the vertical position where the lane line intercepts the y-axis.
        Ending Point: np.int32(np.round((img_shape[0] - lane_right_bias) / lane_right_slope)), img_shape[0] is on the bottom of the image, where the lane line would extend based on its slope.
        By connecting these two points, the code draws a line that approximates the right boundary of the lane, extending from the top to the bottom of the image. This line will represent the right lane boundary in the image, helping to delineate the lane for the lane detection system.

    - Coordinate Calculation for the Left Lane:

        x1, y1 = 0, neg_bias

        x1 = 0: This sets the x-coordinate of the starting point of the left lane line to 0, which corresponds to the left edge of the image.
        y1 = neg_bias: This sets the y-coordinate of the starting point to neg_bias. The neg_bias is the y-intercept of the line, which is the point where the line crosses the y-axis.
        Thus, (0, neg_bias) is a point on the left side of the image where the left lane line starts.

        x2, y2 = -np.int32(np.round(neg_bias / neg_slope)), 0

        x2 = -np.int32(np.round(neg_bias / neg_slope)): This calculates the x-coordinate of the second point of the left lane line by finding where the line intersects the bottom of the image. To find this intersection, the code:

        Divides neg_bias by neg_slope to find the x-coordinate where the line crosses the x-axis (since y = 0).
        Negates this value to get the coordinate in the positive x-direction because the slope is negative.
        Rounds and converts to np.int32 to get integer coordinates suitable for image processing.
        y2 = 0: This sets the y-coordinate of the second point to 0, which corresponds to the bottom of the image (the x-axis in image coordinates).

        Thus, (-np.int32(np.round(neg_bias / neg_slope)), 0) is a point on the bottom of the image where the line representing the left lane would intersect.

        Purpose
        Defining the Line Segment: These calculations are used to define a line segment that represents the left lane boundary. By specifying the starting and ending coordinates of the line segment, you ensure that the line covers the portion of the image where the lane is expected to appear.

        Image Coordinate System: In image coordinates, the origin (0, 0) is at the top-left corner, with x increasing to the right and y increasing downward. The calculations ensure that the line spans from the top to the bottom of the image.

        Visualization
        Starting Point: (0, neg_bias) is on the left side of the image at the vertical position where the lane line intercepts the y-axis.
        Ending Point: (-np.int32(np.round(neg_bias / neg_slope)), 0) is on the bottom of the image, where the lane line would extend based on its slope.
        By connecting these two points, you draw a line that approximates the left boundary of the lane, extending from the top of the image to the bottom.

    - Then stores coordinates of left and right lanev lines in a list by Line(x1,y1,x2,y2).


5. get_lane_lines(color_image, solid_lines=True) -->  This function take as input a color road frame and tries to infer the lane lines in the image.
    :param color_image: input frame
    :param solid_lines: if True, only selected lane lines are returned. If False, all candidate lines are returned.
    :return: list of (candidate) lane lines.
    - The Operations are:
        1. Resize: Resizes the input image to a fixed size of 960x540 pixels. This standardizes the image size for further processing.
        2. Grayscale Conversion: Converts the color image to grayscale using cv2.cvtColor. This simplifies the image, making edge detection easier.
        3. Gaussian Blur: Applies a Gaussian blur with a kernel size of 17x17 to reduce noise and smooth the image. This helps in better edge detection.
        4. Canny Edge Detection: Uses the Canny algorithm to detect edges in the blurred grayscale image. The thresholds (50 and 80) control the sensitivity of the edge detection.
        5. Hough Line Transform: Uses the Hough Transform to detect lines in the edge-detected image and stores in a list.
        6. Convert to Line Objects: Converts the detected lines (represented as tuples of coordinates) into Line objects for easier manipulation and analysis.
        7. Lane Line Selection:
            1. Solid Lines Option:
                Candidate Line Filtering: If solid_lines is True, filter the detected lines to only consider those with slopes between approximately 30 and 60 degrees (converted to slope values between 0.5 and 2). This helps to filter out irrelevant lines and focus on potential lane lines.
                Compute Lane Lines: Calls compute_lane_from_candidates to compute the left and right lane lines from the filtered candidate lines.
            2. All Lines Option:
                If solid_lines is False, return all detected lines without further processing.
        8. Return Value: Returns the final list of lane lines, either the main lane lines (if solid_lines is True) or all detected lines (if solid_lines is False).

6. smoothen_over_time(lane_lines) --> Smooth the lane lines over multiple frames to reduce flickering.
    How it works:
    Accumulate Lines: Collect lines over frames.
    Average Lines: Compute average lane lines over the window of frames.
    Two numpy arrays, avg_line_lt and avg_line_rt, are initialized with zeros. Each array has a shape of (number_of_frames, 4), where 4 represents the coordinates (x1, y1, x2, y2) of a line. Iterate through each set of lane lines detected in the frames. For each frame t, extract the coordinates of the left and right lane lines using get_coords() method and accumulate these coordinates in avg_line_lt and avg_line_rt. Compute the mean of the accumulated coordinates along the axis representing the frames. This results in average coordinates for the left and right lane lines. Create and return Line objects using these average coordinates.

7. color_frame_pipeline(frames, solid_lines=True, temporal_smoothing=True) --> Main function that integrates all previous steps to process a list of frames and overlay detected lanes.
    - The Proccess is as follows :
        1. Original Image:
            Full-color road image or video frame.
        2. Preprocessed Image:
            Grayscale, blurred, and edge-detected.
        3. Detected Lines:
            Lines overlaid on the edge-detected image.
        4. Filtered Lanes:
            Approximate lane lines extracted.
        5. Smoothed Lanes (if applicable):
            Lane lines smoothed over time.
        6. Lane Lines Overlaid:
            Lane lines drawn on the original image.
        7. Final Output:
            The original image with lane lines blended in, showing detected lanes.
    By visualizing each step, you get a clear view of how raw input images are transformed into a final result with lane lines highlighted.
