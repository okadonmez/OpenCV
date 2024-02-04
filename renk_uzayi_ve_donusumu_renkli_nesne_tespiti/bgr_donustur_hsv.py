import cv2
import numpy as np

yesil = np.uint8([[[0,255,0]]])

hsv_yesil = cv2.cvtColor(yesil,cv2.COLOR_BGR2HSV)

print(hsv_yesil)