import cv2


face_cascade = cv2.CascadeClassifier("res/orijinal/haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier("res/orijinal/haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while(1):
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.2,3)

    for(x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(122,55,33),2)
        
    cv2.imshow("Yuz ve Goz Tespiti",frame)
        
    k = cv2.waitKey(30) & 0xFF

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()