import numpy as np
import cv2
from skimage.transform import AffineTransform, warp, resize

im = cv2.imread("res/orijinal/ornek_v1.jpg")

trans = AffineTransform(scale=(1,2))

im2 = warp(im,trans.inverse,mode='constant') #Yapistiriyor resmin ustune
im3 = resize(im, (500,500))

cv2.imshow("Orijinal Resim",im)
cv2.imshow("Afin Resim",im2)
cv2.imshow("Resize Resim",im3) #Ayni resmi bozmadan buyutup kucultmeye yariyor

cv2.waitKey(0)
cv2.destroyAllWindows()