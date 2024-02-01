import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

font = cv2.FONT_HERSHEY_COMPLEX

#cv2.putText(img,'OpenCV',(50,50),font,4,(0,155,255),2,cv2.LINE_AA)
cv2.putText(img,"OpenCV",(0,300),font,4,(0,155,255),2,cv2.LINE_AA)

cv2.imshow("Resim",img)

cv2.waitKey(0)

cv2.destroyAllWindows()