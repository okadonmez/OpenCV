import cv2
import numpy as np


img = cv2.imread("res/orijinal/ornek_v1.jpg")

#gaussian = cv2.GaussianBlur(img,(7,7),0)
gaussian = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow("Normal Resim",img)
cv2.imshow("Gaussian Resim",gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()