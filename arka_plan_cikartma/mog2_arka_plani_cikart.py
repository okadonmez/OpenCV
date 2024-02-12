import cv2


cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret,frame = cap.read()
    
    mask = fgbg.apply(frame)

    cv2.imshow("Normal Video",frame)
    cv2.imshow("Arka Plansiz Video",mask)

    k = cv2.waitKey(30) & 0xFF

    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()