import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Kamera taninmadi.")
    exit()

#ozellik_yazdir = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
ozellik_yazdir = cam.get(3)

print(ozellik_yazdir)

while True:
    ret, frame = cam.read()

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if not ret:
        print("Kameradan goruntu okunamiyor.")
        break

    cv2.imshow("Kamera",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Goruntu sonlandirildi.")
        break

cam.release()

cv2.destroyAllWindows()