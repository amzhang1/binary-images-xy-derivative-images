import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

#Read this gray scale image. Display the image.Compute gradient of the image by Sobel edge operators - you will apply filtering here to compute the gradient, i.e. you will construct a kernel and use cv2.filter2D rather than cv2.Sobel. Display the horizontal and vertical direction derivative images. Compute gradient magnitude image by suitably combining the horizontal and the vertical derivative images. Display the gradient magnitude image.

img = cv2.imread('ex2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # convert to grayscale

kernelx = np.zeros((3,3), np.float32)#filter for x derivative image
kernelx[0][0] = -1;
kernelx[0][1] = 0;
kernelx[0][2] = 1;
kernelx[1][0] = -2;
kernelx[1][2] = 2;
kernelx[2][0] = -1;
kernelx[2][2] = 1;
kernely = np.zeros((3,3), np.float32)#filter for y derivative image
kernely[0][0] = -1;
kernely[0][1] = -2;
kernely[0][2] = -1;
kernely[2][0] = 1;
kernely[2][1] = 2;
kernely[2][2] = 1;

#print(kernelx) # for testing
#print(kernely) # for testing

horizontal = cv2.filter2D(img,-1,kernelx) # convolutes the image with the kernelx, given the source image, depth of the destination image, and the 3x3 matrix
vertical = cv2.filter2D(img,-1,kernely) # convolutes the image with the kernelx, given the source image, depth of the destination image, and the 3x3 matrix

gradient = np.absolute(horizontal) + np.absolute(vertical)

plt.figure(1)

plt.subplot(221)
plt.imshow(img, 'gray') #grayscale image
plt.title('Original')

plt.subplot(222)
plt.imshow(horizontal, 'gray') #(x) horizontal direction derivative image
#plt.imshow(horizontal)
plt.title('X derivative')

plt.subplot(223)
plt.imshow(vertical, 'gray') #(y) vertical direction derivative image
#plt.imshow(vertical)
plt.title('Y derivative')

plt.subplot(224)
plt.imshow(gradient, 'gray') #gradient magnitude image
#plt.imshow(gradient_final, 'gray') #gradient magnitude image
plt.title('Gradient magnitude')

plt.show()