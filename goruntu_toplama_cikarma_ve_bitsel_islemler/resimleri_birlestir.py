import cv2
import numpy as np


img1 = cv2.imread("res/orijinal/ornek_v1.jpg")
img2 = cv2.imread("res/orijinal/ornek_v2.jpg")


x,y,z = img1.shape
roi = img2[0:x,0:y] #2. resimden 1. resimin alani kadar bir alani kirpiyoruz.


img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) # Kirptiktan sonra 1. resimi griye ceviriyoruz.
ret, mask = cv2.threshold(img1_gray,10,255,cv2.THRESH_BINARY) #10 piksele kadar olan degerleri al gerisini 255 yap ve mask'a yukle dedik. Yani maskeledik renkli degerleri.


mask_inv = cv2.bitwise_not(mask) #Bu maskeyi de ters cevirerek invert cevirilmis resim diyerek kayit ediyoruz.


img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv) #Yanlis bitsel carpma yapmamak icin sayiyi kendisi ile carpiyoruz.

img2_fg = cv2.bitwise_and(img1,img1,mask=mask)


toplam = cv2.add(img1_bg,img2_fg) #Elde ettigimiz resimleri birlestiriyoruz.


img2[0:x,0:y] = toplam


cv2.namedWindow("Resim1",cv2.WINDOW_NORMAL)

cv2.imshow("Resim1",img1)
cv2.imshow("Resim2",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()