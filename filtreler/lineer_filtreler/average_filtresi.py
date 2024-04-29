import cv2
import numpy as np


img = cv2.imread("res/orijinal/ornek_v4.jpg")

#kernel = np.ones((5,5),np.float32)/25
#kernel = np.ones((5,5),np.float32)/15 #Cok daha kotu oldu.
#kernel = np.ones((5,5),np.float32)/35 #Arttirdikca puruzler azalmaya basliyor.
kernel = np.ones((3,3),np.float32)/25 #(3,3) parametresi ile goruntu daha da netlesti.

after_filter = cv2.filter2D(img,-1,kernel)

cv2.imshow("Normal Resim",img)
cv2.imshow("Average Resim",after_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()