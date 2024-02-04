import cv2
import numpy as np


img1 = cv2.imread("res/orijinal/ornek_v1.jpg")
img2 = cv2.imread("res/orijinal/ornek_v2.jpg")

toplam = cv2.addWeighted(img1,0.7,img2,0.3,0) #img1 * 0.7 + img2 * 0.3 + 0.

cv2.imshow("Resim",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()