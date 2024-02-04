import cv2
import numpy as np

camera = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow("Frame")

cv2.createTrackbar("H1","Frame",0,359,nothing)
cv2.createTrackbar("H2","Frame",0,359,nothing)
cv2.createTrackbar("S1","Frame",0,255,nothing)
cv2.createTrackbar("S2","Frame",0,255,nothing)
cv2.createTrackbar("V1","Frame",0,255,nothing)
cv2.createTrackbar("V2","Frame",0,255,nothing)

while camera.isOpened():
    _, frame = camera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    H1 = int(cv2.getTrackbarPos("H1","Frame") / 2)
    H2 = int(cv2.getTrackbarPos("H2","Frame") / 2)
    S1 = cv2.getTrackbarPos("S1","Frame")
    S2 = cv2.getTrackbarPos("S2","Frame")
    V1 = cv2.getTrackbarPos("V1","Frame")
    V2 = cv2.getTrackbarPos("V2","Frame")

    lower = np.array([H1,S1,V1]) #[H,S,V]
    upper = np.array([H2,S2,V2])

    mask = cv2.inRange(hsv,lower,upper) #110 ile 130 arasinaki araligi aliyor. Normalde 120'yi istiyoruz ama araliklar cok yakin olduugu icin digerlerini de aliyoruz.

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Frame",frame)
    cv2.imshow("HSV",mask)
    cv2.imshow("Res",res)

    if cv2.waitKey(5) == ord("q"):
        break

cv2.destroyAllWindows()