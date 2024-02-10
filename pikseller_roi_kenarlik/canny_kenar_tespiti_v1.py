import cv2
import numpy as np


img = cv2.imread("res/orijinal/ornek_v1.jpg")

edge = cv2.Canny(img,100,200)

cv2.imshow("Normal Resim",img)
cv2.imshow("Kenarli Resim",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()