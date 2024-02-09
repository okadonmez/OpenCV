import cv2


img = cv2.imread("res/orijinal/ornek_v1.jpg",0)

ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow("Resim",img)
cv2.imshow("Resim Thresh",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()