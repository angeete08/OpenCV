import cv2 as cv

#Read and display images
'''img = cv.imread('resources/tiger.jpg')
cv.imshow('Tiger', img)
cv.waitKey(0)'''

#---------------------------------------------------------------------------------------

#Reading Videos
#cv.VideoCapture will use int arguments if you want to use webcam or camera
#Webcam: 0
#1st connected camera: 1
#...
#Note that capture is a pointer to the video
capture = cv.VideoCapture(0)

#Reads in video frame by frame until no frames are left
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

#0xFF is a hexadecimal constant which is 11111111 in binary.
#If d is pressed, break out of loop and stop video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#Relasing ptr releases memory just like delete in c++
capture.release()
cv.destroyAllWindows()

#Error 215 if we reach the end of video and cv can't find the next frame or if we give the wrong path for images
#-------------------------------------------------------------------------------------------------


