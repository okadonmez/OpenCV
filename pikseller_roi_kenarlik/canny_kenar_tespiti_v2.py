import cv2


img = cv2.imread("res/orijinal/ornek_v1.jpg",0)

edges = cv2.Canny(img,127,255)

cv2.imshow("Resim",img)
cv2.imshow("Resim Canny",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()