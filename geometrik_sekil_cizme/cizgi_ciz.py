import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(512,512),(255,0,0),5)
cv2.line(img,(128,384),(384,128),(0,255,0),15)

cv2.imshow("Resim",img)

cv2.waitKey(0)

cv2.destroyAllWindows()