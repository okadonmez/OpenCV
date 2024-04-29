import cv2
import numpy as np
import scipy.ndimage

img = cv2.imread("res/orijinal/ornek_v1.jpg",0)

k = np.ones((3,3))/9
max = scipy.ndimage.filters.maximum_filter(img,size=5)

cv2.imshow("Normal Resim",img)
cv2.imshow("Maximum Resim",max)

cv2.waitKey(0)
cv2.destroyAllWindows()