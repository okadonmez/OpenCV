import cv2


cap = cv2.VideoCapture(0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorKNN()

while(1):
    ret,frame = cap.read()
    
    mask = fgbg.apply(frame)

    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    cv2.imshow("Normal Video",frame)
    cv2.imshow("Arka Plansiz Video",mask)

    k = cv2.waitKey(30) & 0xFF

    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()