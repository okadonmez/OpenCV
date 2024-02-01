import cv2

cam = cv2.VideoCapture(0)

print("Ilk genislik: " + str(cam.get(3)))
print("Ilk yukseklik: " + str(cam.get(4)))

cam.set(3,320)
cam.set(4,240)

print("\n")

print("Son genislik: " + str(cam.get(3)))
print("Son yukseklik: " + str(cam.get(4)))

if not cam.isOpened():
    print("Kamera taninmadi.")
    exit()

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