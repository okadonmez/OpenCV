import cv2


#img = cv2.imread("res/orijinal/ornek_v1.jpg")
img = cv2.imread("res/orijinal/ornek_v3.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 177, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
area = cv2.contourArea(cnt)

print(area)

perimeter = cv2.arcLength(cnt,True)

print(perimeter)

cv2.imshow("Resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()