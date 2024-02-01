import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

cv2.circle(img,(255,255),100,(0,0,255),15) #Cember.
cv2.circle(img,(255,255),50,(200,200,200),-1) #Daire.

cv2.imshow("Resim",img)

cv2.waitKey(0)

cv2.destroyAllWindows()