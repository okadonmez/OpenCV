import cv2


img1 = cv2.imread("res/orijinal/ornek_v1.jpg")
img2 = cv2.imread("res/orijinal/ornek_v3.jpg")

bitwise_or = cv2.bitwise_or(img1,img2)

cv2.imshow("Resim 1",img1)
cv2.imshow("Resim 2",img2)
cv2.imshow("Resim Or",bitwise_or)

cv2.waitKey(0)
cv2.destroyAllWindows()