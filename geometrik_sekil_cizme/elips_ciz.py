import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

cv2.ellipse(img,(255,255),(100,50),0,0,180,(0,0,255),15) #Ici bos, sadece cizgiler var.
cv2.ellipse(img,(255,255),(80,25),0,0,180,(200,200,200),-1) #Ici dolu.

cv2.imshow("Resim",img)

cv2.waitKey(0)

cv2.destroyAllWindows()