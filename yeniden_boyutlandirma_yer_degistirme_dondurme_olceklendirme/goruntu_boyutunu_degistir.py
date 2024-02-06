import cv2


img = cv2.imread("res/orijinal/ornek_v1.jpg")

print(img.shape)

#res = cv2.resize(img,(300,300))
#res = cv2.resize(img,None,fx=1,fy=1)
#res = cv2.resize(img,None,fx=1.5,fy=1) #Oranlari degistirdigimizde ornegin orani arttirdigimizda pikseller oralama bulma yontemiyle ekleniyor. Bunun icin matrisler kullanilir. Matrisel carpim islemi yapiliyor. Buna interpolation yontemi denir.
res = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC) #Cubic en yavas olanidir ama sonucu en dogru sekilde verir. Boyutlandirma islemlerinde, filtrelerde, yuz ve goz tespitinde vs. kullanilir.

cv2.imshow("Resim",img)
cv2.imshow("Res",res)

cv2.waitKey()
cv2.destroyAllWindows()