import cv2
import numpy as np


img = cv2.imread("res/orijinal/ornek_v1.jpg")

mean = cv2.medianBlur(img,7)

cv2.imshow("Normal Resim",img)
cv2.imshow("Mean Resim",mean)

cv2.waitKey(0)
cv2.destroyAllWindows()