#importing data using openCV

import cv2 as cv
import numpy as np
image1 = cv.imread(“image_name_with_its_path”)
image1.imshow()

#converting image to gray scale
import cv2 as cv
image = cv.imread(“image_name_with_path”)
x = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow(‘GrayScale Image’, x)

#applying various threshold transitions to image

import cv2 as cv
import numpy as np
image = cv.imread(“Image_path_name”)
img = cv.cvtColor(image, cv.RGB2GRAY)
ret, thresh1 = cv.threshold(img, 120, 255, cv.THRES_BINARY)
ret, thresh2 = cv.threshold(img, 120, 255, cv.THRES_BINARY_INV)
ret, thresh3 = cv.threshold(img, 120, 255, cv.THRES_TRUNC)
