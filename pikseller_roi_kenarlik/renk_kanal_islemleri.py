import cv2
import matplotlib.pyplot as plt


resim = cv2.imread("res/orijinal/ornek_v1.jpg")

b,g,r = cv2.split(resim)

print(b,g,r)

resim2 = cv2.merge((b,g,r))

b = resim[:,:,0] #Blue kanalini tamamen al.

resim[:,:,2] = 0 #Resmin butun kanallarini al Red'i alma.

cv2.imshow("Resim",resim)

cv2.waitKey(0)
 
cv2.destroyAllWindows()