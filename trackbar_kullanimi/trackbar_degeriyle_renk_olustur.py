import cv2
import numpy as np


def nothing(x):
    pass

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow("Resim")

cv2.createTrackbar("R Kontrolu","Resim",0,255,nothing)
cv2.createTrackbar("G Kontrolu","Resim",0,255,nothing)
cv2.createTrackbar("B Kontrolu","Resim",0,255,nothing)

while(1):
    cv2.imshow("Resim",img)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    
    r = cv2.getTrackbarPos("R Kontrolu","Resim")
    g = cv2.getTrackbarPos("G Kontrolu","Resim")
    b = cv2.getTrackbarPos("B Kontrolu","Resim")

    img[:] = [b,g,r]

cv2.destroyAllWindows()