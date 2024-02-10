import cv2
import numpy as np


img = cv2.imread("res/orijinal/ornek_v4.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

GRAY = np.float32(gray)

#dst = cv2.cornerHarris(GRAY,2,3,0.03)
dst = cv2.cornerHarris(GRAY,5,3,0.04)

img[dst>0.01*dst.max()] = [0,255,0]

cv2.imshow("Harris Resim",img)

cv2.waitKey(0)
cv2.destroyAllWindows()