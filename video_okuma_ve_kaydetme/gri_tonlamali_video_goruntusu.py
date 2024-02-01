import cv2

cam = cv2.VideoCapture("res/orijinal/ornek_v2.mp4")

while cam.isOpened():
    ret, frame = cam.read()

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if not ret:
        print("Kameradan  goruntu okunamiyor.")
        break
    
    cv2.imshow("Goruntu",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Video kapatildi.")
        break

cam.release()
cv2.destroyAllWindows()