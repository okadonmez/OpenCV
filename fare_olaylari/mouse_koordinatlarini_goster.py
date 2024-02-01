import cv2
import numpy as np


def draw(event,x,y,flags,param): #Klavye hareketlerini icine tanimliyacagimiz fonksiyon.
    print("Mouse x: " + str(x),"  Mouse y: " + str(y))
    pass

img = np.ones((512,512,3),np.uint8)

cv2.namedWindow("Paint")

cv2.setMouseCallback("Paint",draw)

while(1):
    cv2.imshow("Paint",img)

    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break

cv2.destroyAllWindows()