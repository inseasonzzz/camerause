# -*- coding: utf-8 -*-
import cv2 as cv
import time
import RPi.GPIO as GPIO
GPI0.setmode (GPI0.B0ARD)
GPIO.setup(13, GPIO.IN, pull_up_down=GPI0.PUD_DOWN)
capture = cv .VideoCapture(0)
index = 0

while(True) :
    if(GPI0. input(13) == 1) :
        print(1)
        #capture = cv.VideoCapture(0)
        ret, frame = capture. read()
        #gray = cv.cvtColor(frame， CV.COLOR_ BGR2GRAY) ;
        cv . imshow( "video", frame)
        cv . imwrite(str( index)+" .jpg", frame)
        index+=1
        cv .waitKey (500)
    else:
        print(0)
        cv .destroyAllWindows()
    time.sleep(0.5)
