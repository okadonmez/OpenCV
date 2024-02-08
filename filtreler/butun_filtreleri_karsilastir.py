import cv2
import numpy as np


img = cv2.imread("res/orijinal/ornek_v3.jpg")

kernel = np.ones((7,7),np.float32)/25

after_filter = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(7,7))
gaussian = cv2.GaussianBlur(img,(7,7),0)
mean = cv2.medianBlur(img,7)

cv2.imshow("Normal Resim",img)
cv2.imshow("Average Resim",after_filter)
cv2.imshow("Blur Resim",blur)
cv2.imshow("Gaussian Resim",gaussian)
cv2.imshow("Mean Resim",mean)

cv2.waitKey(0)
cv2.destroyAllWindows()