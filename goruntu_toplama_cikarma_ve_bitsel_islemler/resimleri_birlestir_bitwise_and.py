import cv2


img1 = cv2.imread("res/orijinal/ornek_v1.jpg")
img2 = cv2.imread("res/orijinal/ornek_v3.jpg")

bitwise_and = cv2.bitwise_and(img1,img2)

cv2.imshow("Resim 1",img1)
cv2.imshow("Resim 2",img2)
cv2.imshow("Resim And",bitwise_and)

cv2.waitKey(0)
cv2.destroyAllWindows()