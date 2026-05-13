import cv2
import numpy as np
video = cv2.VideoCapture('video1 (1).avi')
car_cascade = cv2.CascadeClassifier('cars.xml')
while True:
    exit_value,current_frame = video.read()
    if exit_value == False:
        break
    gray_image = cv2.cvtColor(current_frame,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray_image,1.1,1)
    for (x,y,w,h) in cars:
        circular_img = cv2.circle(gray_image,(x+w//2,y+h//2),w//2,(0,0,255),2)
    cv2.imshow("Car Detection",gray_image)
    if cv2.waitKey(33) == 27:
        break
cv2.destroyAllWindows()





