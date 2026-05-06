import cv2
import numpy as np
import time
og_vid = cv2.VideoCapture("video.mp4")
time.sleep(3)
count = 0
bg = 0

for i in range(60):
    exit_value,bg = og_vid.read()
    if exit_value == False:
        continue

bg = np.flip(bg, axis = 1)

while(og_vid.isOpened()):
    exit_value,current_frame = og_vid.read()
    count = count + 1
    current_frame = np.flip(current_frame, axis = 1)
    HSV_frame = cv2.cvtColor(current_frame,cv2.COLOR_BGR2HSV)

    lower_red = np.array([100, 40, 40])       
    upper_red = np.array([100, 255, 255])
    mask1 = cv2.inRange(HSV_frame, lower_red, upper_red)
    
    lower_red = np.array([155, 40, 40])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(HSV_frame, lower_red, upper_red)
    
    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3),
                                         np.uint8), iterations = 2)
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations = 1)
    mask2 = cv2.bitwise_not(mask1)

    result1 = cv2.bitwise_and(bg, bg, mask = mask1)
    result2 = cv2.bitwise_and(HSV_frame, HSV_frame, mask = mask2)
    final_output = cv2.addWeighted(result1,1,result2,1,0)
    
    cv2.imshow("INVISIBLE MAN", final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break






