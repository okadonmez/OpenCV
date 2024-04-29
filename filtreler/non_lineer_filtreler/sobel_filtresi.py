import cv2
import numpy as np
import scipy.ndimage

img = cv2.imread("res/orijinal/ornek_v4.jpg",0)

k = np.ones((3,3))/9
img_sobel = scipy.ndimage.sobel(img)

cv2.imshow("Normal Resim",img)
cv2.imshow("Sobel Resim",img_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()