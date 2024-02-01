import cv2

resim = cv2.imread("res/orijinal/ornek_v1.jpg")

cv2.imshow("Resim Penceresi", resim)

k = cv2.waitKey(0)

print(k)

cv2.destroyWindow("Resim Penceresi")