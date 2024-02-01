import cv2

resim = cv2.imread("res/orijinal/ornek_v1.jpg",0)

cv2.imshow("Resim Penceresi", resim)

cv2.waitKey(0)

cv2.destroyWindow("Resim Penceresi")