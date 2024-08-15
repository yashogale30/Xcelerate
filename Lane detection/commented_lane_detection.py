import matplotlib.pyplot as plt
import cv2
import os
from os.path import join, basename
from collections import deque
from lane_detection import color_frame_pipeline
#imported necessary libraries and color_frame_pipeline from lane_detection file


if __name__ == '__main__':

    resize_h, resize_w = 540, 960
    #Set the dimesions of frames

    verbose = True
    if verbose:
        plt.ion()
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        #Maximize the window

    # test on images
    test_images_dir = join('data', 'test_images')
    test_images = [join(test_images_dir, name) for name in os.listdir(test_images_dir)]
# A list of image paths is created - test_images

#A loop that iterates over the list
    for test_img in test_images:
        
        #prints the path
        print('Processing image: {}'.format(test_img))

        #returns only base name
        out_path = join('out', 'images', basename(test_img))
        #converts from bgr to rbg
        in_image = cv2.cvtColor(cv2.imread(test_img, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
        out_image = color_frame_pipeline([in_image], solid_lines=True)
        #calls out function to detect lines
        cv2.imwrite(out_path, cv2.cvtColor(out_image, cv2.COLOR_RGB2BGR))
        #image is then saved to directory

        #the image is displayed
        if verbose:
            plt.imshow(out_image)
            plt.waitforbuttonpress()
    plt.close('all')
    #To close everything



    # test on videos
    test_videos_dir = join('data', 'test_videos')
    test_videos = [join(test_videos_dir, name) for name in os.listdir(test_videos_dir)]
#makes a similar list to store videos from dataset


    for test_video in test_videos:

        print('Processing video: {}'.format(test_video))

        cap = cv2.VideoCapture(test_video)
        out = cv2.VideoWriter(join('out', 'videos', basename(test_video)),
                              fourcc=cv2.VideoWriter_fourcc(*'DIVX'),
                              fps=20.0, frameSize=(resize_w, resize_h))
        
        #The processed video is stored


        #the same thing is done for frames of video , the processed frame is displayed for 1ms

        frame_buffer = deque(maxlen=10)
        while cap.isOpened():
            ret, color_frame = cap.read()
            if ret:
                color_frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB)
                color_frame = cv2.resize(color_frame, (resize_w, resize_h))
                frame_buffer.append(color_frame)
                blend_frame = color_frame_pipeline(frames=frame_buffer, solid_lines=True, temporal_smoothing=True)
                out.write(cv2.cvtColor(blend_frame, cv2.COLOR_RGB2BGR))
                cv2.imshow('blend', cv2.cvtColor(blend_frame, cv2.COLOR_RGB2BGR)), cv2.waitKey(1)
            else:
                break
        cap.release()
        out.release()
        #everthing is released
        cv2.destroyAllWindows()



