# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:24:41 2018

@author: fjiangqing
"""

import cv2

clicked = False

def omMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_FLAG_LBUTTON:
        clicked = True

cameraCapture = cv2.VideoCapture(0)

#cv2.namedWindow('myWindows')
#cv2.setMouseCallback('myWindow', onMouse)

print('Showing camera feed. Click window or pres any to stop')

success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow("myWindow", frame)
    success, frame = cameraCapture.read()
    
cv2.destroyAllWindows()
cameraCapture.release()