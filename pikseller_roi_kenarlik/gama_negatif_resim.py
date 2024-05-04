import cv2
import numpy as np

img = cv2.imread("res/orijinal/ornek_v4.jpg",0)
gamma = 0.5

img2 = img.astype(float)
img3 = np.array(255.0*(img2/255)**gamma,dtype='uint8')

cv2.imshow("Normal Resim",img)
cv2.imshow("Negatif Donusum Resim",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()