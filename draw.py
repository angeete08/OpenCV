import cv2 as cv
import numpy as np

#Cretes a blank image screen, default color is black
#Height, Width, Color Channel = 500,500,3
blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)

#Paint image a certain color
#Order of color channels is actually BGR
blank[:] = 0,165,255
#cv.imshow('Red', blank)

#Color in a certain range of pixels
#blank[200:300,300:400] = 255,0,0
#cv.imshow('Red', blank)

#----------------------------------------------------------------------------------------------------------------------

#Draw a Rectangle
#Image, point1, point2, color, border thickness: blank, (0,0), (250,250), (0,255,0), thickness=2
#cv.FILLED fills the entire rectangle with that color, or you can use thickness=-1
#cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
#cv.imshow('Rectangle', blank)

#You can also draw a rectangle based of main image size, HOWEVER, YOU MUST USE INT VALUES -> //2
#Otherwise you will get an error
#cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[1]//2), (0,255,0), thickness=cv.FILLED)
#cv.imshow('Rectangle', blank)

#-----------------------------------------------------------------------------------------------------------------------

#Draw a Circle, note there is also a cv.ellipse
#Image, center, radius, color, thickness
#cv.circle(blank, (250,250), 40, (255,0,0), thickness=-1)
#cv.imshow('Circle', blank)

#-----------------------------------------------------------------------------------------------------------------------
#Draw a line, if start and end pt are same, you can draw a point
#Image, point1, point2, color, thickness = blank, (0,0), (blank.shape[1]//2,blank.shape[1]//2), (0,255,0), thickness=cv.FILLED
cv.line(blank, (0,0), (500,500), (255,255,255), thickness=3)
#cv.imshow('Line', blank)

#-----------------------------------------------------------------------------------------------------------------------
#Put text on an image
#Image, text, origin, font, font scale
cv.putText(blank, 'hello', (210,210), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)
