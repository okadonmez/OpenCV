import cv2
import numpy as np


img = cv2.imread("res/orijinal/ornek_v1.jpg")

rows,cols = img.shape[:2]


#rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)
rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),30,0.7)

#img_rotation = cv2.warpAffine(img,rotation_matrix,(cols,rows))
img_rotation = cv2.warpAffine(img,rotation_matrix,(int(cols*1.2),int(rows*1.2)))


cv2.imshow("Resim",img)
cv2.imshow("Resim Translation",img_rotation)

cv2.waitKey()
cv2.destroyAllWindows()