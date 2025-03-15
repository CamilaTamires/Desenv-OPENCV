import cv2
import numpy as np

img1 = cv2.imread ('001.png')
img2 = cv2.imread ('mascara-rectangle.png')

img_and = cv2.bitwise_and(img1, img2)
img_or = cv2.bitwise_or(img1, img2)
img_xor = cv2.bitwise_xor(img1,img2)
img_not = cv2.bitwise_not(img1)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('land2',img_and)
cv2.imshow('lor2',img_or)
cv2.imshow('lxor',img_xor)
cv2.imshow('not1',img_not)
cv2.waitKey(0)