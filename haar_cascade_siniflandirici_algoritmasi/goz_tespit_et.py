import cv2


img = cv2.imread("res/orijinal/ornek_v6.jpg")

eyes_cascade = cv2.CascadeClassifier("res/orijinal/haarcascade_eye.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

eyes = eyes_cascade.detectMultiScale(gray,1.3,7) #Burasi ne kadar yuksek olursa o kadar cerceve ekliyor ve daha net bir algilama gerceklestiriyor.

for (x,y,w,h) in eyes:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow("Goz Tespiti",img)
cv2.waitKey(0)
cv2.destroyAllWindows()