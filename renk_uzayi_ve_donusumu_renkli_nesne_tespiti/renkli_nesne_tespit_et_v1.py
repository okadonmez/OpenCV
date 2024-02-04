import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while camera.isOpened():
    _, frame = camera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([110,50,50]) #[H,S,V]
    upper = np.array([130,255,255]) #Ikinci ve ucuncu degerler genelde 50'den baslar ve 255'e kadar gider. Renk tonuna kalmistir. Parlaklik ve doygunlugumuza gore degisir.

    mask = cv2.inRange(hsv,lower,upper) #110 ile 130 arasinaki araligi aliyor. Normalde 120'yi istiyoruz ama araliklar cok yakin oldugu icin digerlerini de aliyoruz. Genelde istenen rengin 10 eksigi ve 10 fazlasi yazilir. Tercihen artabilir -20, +20 yapan da vardir.

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Frame",frame)
    cv2.imshow("HSV",mask)
    cv2.imshow("Res",res)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()