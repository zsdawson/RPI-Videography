#script1
import cv2 as cv
import matplotlib as plt

img = cv.imread('/Users/zacharydawson/Desktop/RPI-Videography-main/images/moth1.jpeg')

cv.imshow('moth1', img)

# this is for use with a video feed 
#capture = cv.VideoCapture(0) 

#grey picture to see paterns not colors 
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#edge image
canny = cv.Canny(img, 125, 175)
cv.imshow('canny edges', canny)


cv.waitKey(0)

plt.imshow(img)

plt.show()




