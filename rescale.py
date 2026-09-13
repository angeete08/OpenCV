import cv2 as cv

#Rescales width and height, works for both images and videos
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

#ONLY WORKS FOR LIVE VIDEO, NOT FOR PREEXISTING VIDEO
def changeRes(width,height):
    #3 represents width
    #4 represents height
    capture.set(3,width)
    capture.set(4,height)

img = cv.imread('resources/tiger.jpg')
img_resized = rescaleFrame(img,0.75)
cv.imshow('Tiger', img)

#We only move to next part of code if we press 0
cv.waitKey(0)

#Captures video, resises it and then displays it
capture = cv.VideoCapture('resources/small_plane.MP4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.5)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
