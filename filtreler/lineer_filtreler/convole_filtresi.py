import cv2
import numpy as np
import scipy.ndimage

img = cv2.imread("res/orijinal/ornek_v1.jpg",0)

k = np.ones((3,3))/9
b = scipy.ndimage.filters.convole(img,k,mode='constant',cval=0.0)

cv2.imshow("Normal Resim",img)
cv2.imshow("Convole Resim",b)

cv2.waitKey(0)
cv2.destroyAllWindows()