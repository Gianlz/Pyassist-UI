import cv2
from mss import mss
import numpy as np
import win32api
import serial
import os
from main import *


def Colaim(fov, value):
    os.system("cls")
    '''
        TODO 
        custom arduino COM input
        custom HSV color
        headlock (Extreme Opencv Points)  
    '''
    sct = mss()

    # Change your COM
    arduino = serial.Serial("COM3", 115200)

    screenshot = sct.monitors[1]
    screenshot['left'] = int((screenshot['width'] / 2) - (fov / 2))
    screenshot['top'] = int((screenshot['height'] / 2) - (fov / 2))
    screenshot['width'] = fov
    screenshot['height'] = fov
    mid = fov/2

    lower = np.array([140,111,160])
    upper = np.array([148,154,194])


    xspeed = float(input("X Speed (Default 0.1) :"))
    yspeed = float(input("Y Speed (Default 0.1) :"))
    print("Running!, press Ctrl to aim")

    def mousemove(x,y):
        if x < 0: 
            x = x+256 
        if y < 0:
            y = y+256 

        pax = [int(x),int(y)]
        arduino.write(pax)


    while True:
        if win32api.GetAsyncKeyState(value) < 0:
            
            img = np.array(sct.grab(screenshot))
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower,upper)
            kernel = np.ones((3,3), np.uint8)
            dilated = cv2.dilate(mask,kernel,iterations= 5)
            thresh = cv2.threshold(dilated, 60, 255, cv2.THRESH_BINARY)[1]
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            if len(contours) != 0:
                M = cv2.moments(thresh)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                x = -(mid - cX) if cX < mid else cX - mid
                y = -(mid - cY) if cY < mid else cY - mid
                
                
                x2 = x *xspeed
                y2 = y *yspeed
                mousemove(x2,y2)
