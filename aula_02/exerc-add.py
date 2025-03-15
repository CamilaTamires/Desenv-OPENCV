import cv2
import numpy as np

img1 = cv2.imread('mascara-circle.png')
img2 = cv2.imread('mascara-rectangle.png')
imgfinal = cv2.add(img2,img1)

cv2.imwrite("imgfinal-add.png",imgfinal)

