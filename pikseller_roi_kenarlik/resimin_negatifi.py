import cv2
import numpy as np

#img = cv2.imread("res/orijinal/ornek_v1.jpg",cv2.IMREAD_GRAYSCALE)
img = cv2.imread("res/orijinal/ornek_v4.jpg",cv2.IMREAD_COLOR)
img2 = 255 - img

cv2.imshow("Normal Resim",img)
cv2.imshow("Negatif Donusum Resim",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()