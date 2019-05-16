
# coding: utf-8

# In[ ]:


import numpy as np
import cv2

img = cv2.imread('12.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('12.jpg',cv2.IMREAD_COLOR)
images = []
images.append(img)
row,col,_ = img.shape
img = cv2.pyrUp(img);
images.append(img)
distrow = (int)(row*0.1)
distcol = (int)(col*0.1)
img = img[0+distrow:row-distrow,0+distcol:col-distcol]
grayimage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
grayimage2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

sobelX = cv2.Sobel(grayimage,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(grayimage,cv2.CV_64F,0,1)

sobelX2 = cv2.Sobel(grayimage2,cv2.CV_64F,1,0)
sobelY2 = cv2.Sobel(grayimage2,cv2.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelX2 = np.uint8(np.absolute(sobelX2))
sobelY2 = np.uint8(np.absolute(sobelY2))

grayimage = sobelX + sobelY

grayimage2 = sobelX2 + sobelY2

cv2.imshow('add',grayimage)
#cv2.imshow('add2',grayimage2)

grayimage = cv2.GaussianBlur(grayimage,(9,9),0)

grayimage2 = cv2.GaussianBlur(grayimage2,(11,11),0)
#grayimage2 = cv2.bilateralFilter(grayimage2,60,100,10)
#grayimage = cv2.pyrMeanShiftFiltering(img, 2, 10,img, 4)
_,th = cv2.threshold(grayimage,40,255,0)
_,th2 = cv2.threshold(grayimage2,60,255,0)
arr =[]
arr2 =[]
countp=0
cv2.imshow('th',th)
cv2.waitKey(0)
cv2.destroyALLWindows()
#cv2.imshow('th2',th2)

