import cv2

resim = cv2.imread("res/orijinal/ornek_v1.jpg")

print(resim)

cv2.imshow("Resim Penceresi", resim)

cv2.waitKey(0) #Bekleme, bir tusa basilana kadar devam eder.

cv2.destroyWindow("Resim Penceresi")