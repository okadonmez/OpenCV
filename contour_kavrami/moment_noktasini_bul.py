import cv2


img = cv2.imread("res/orijinal/ornek_v4.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

M = cv2.moments(thresh)

x = int(M["m10"]/M["m00"])
y = int(M["m01"]/M["m00"])

cv2.circle(img,(x,y),5,(124,127,21),-1)

cv2.imshow("Moment Noktasi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()