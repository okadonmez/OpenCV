import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

cv2.rectangle(img,(100,100),(200,200),(0,0,255),15) #Ici bos, sadece cizgiler var.
cv2.rectangle(img,(300,300),(350,350),(255,255,0),-1) #Ici dolu.

cv2.imshow("Resim",img)

cv2.waitKey(0)

cv2.destroyAllWindows()