import cv2


camera = cv2.VideoCapture(0)

while camera.isOpened():
    _, frame = camera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow("Frame",frame)
    cv2.imshow("hsv",hsv)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()