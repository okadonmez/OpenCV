import cv2
import numpy as np
import scipy.ndimage

img = cv2.imread("res/orijinal/ornek_v4.jpg",0)

k = np.ones((3,3))/9
img_gaussian = scipy.ndimage.gaussian_laplace(img,sigma=5)

cv2.imshow("Normal Resim",img)
cv2.imshow("Gaussian Resim",img_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()