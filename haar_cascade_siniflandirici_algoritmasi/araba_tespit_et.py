import cv2


car_cascade = cv2.CascadeClassifier("res/orijinal/cars.xml")

cap = cv2.VideoCapture("res/orijinal/ornek_v5.mp4")

while(1):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #cars = car_cascade.detectMultiScale(gray,1.2,3)
    #cars = car_cascade.detectMultiScale(gray,1.2,1)
    cars = car_cascade.detectMultiScale(gray,1.5,1)
    
    for(x,y,w,h) in cars:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    cv2.imshow("Arabalar",frame)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()