import cv2
import numpy as np
from matplotlib import pyplot as plt

# Study and run the code provided here for Canny edge detection.
# Write a small application to find the Canny edge detection whose threshold values can be varied using two track bars. This way, you can understand the effect of threshold values."

def track_min(x):
	global img
	maxVal = cv2.getTrackbarPos('Threshold2','Canny Edge Detection')
	edges = cv2.Canny(img,x,maxVal)
	cv2.imshow('Canny Edge Detection', edges)

def track_max(y):
	global img
	minVal = cv2.getTrackbarPos('Threshold1','Canny Edge Detection')
	edges = cv2.Canny(img,minVal,y)
	cv2.imshow('Canny Edge Detection', edges)


img = cv2.imread('ex2.jpg', 0)
cv2.imshow('Canny Edge Detection',img)

# Create a named window
cv2.namedWindow('Canny Edge Detection')

# create trackbars for minVal and maxVal change
# name of trackbad, named window, value of start, max range, when change happens
# we call nothing
cv2.createTrackbar('Threshold1','Canny Edge Detection',0,255,track_min)
cv2.createTrackbar('Threshold2','Canny Edge Detection',0,255,track_max)

k = cv2.waitKey(0) & 0xFF
