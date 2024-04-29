import cv2
import numpy as np


img = cv2.imread("res/orijinal/ornek_v1.jpg")

kernel = np.ones((5,5),np.float32)/25

blur = cv2.blur(img,(5,5))

cv2.imshow("Normal Resim",img)
cv2.imshow("Blur Resim",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()