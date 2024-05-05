import cv2
import numpy as np

img = cv2.imread("res/orijinal/ornek_v4.jpg",0)
c = 50

logimg = c * (np.log(img+1))
logimg = np.array(logimg,dtype='uint8')


cv2.imshow("Normal Resim",img)
cv2.imshow("Negatif Donusum Resim",logimg)

cv2.waitKey(0)
cv2.destroyAllWindows()