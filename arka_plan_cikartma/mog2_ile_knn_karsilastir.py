import cv2


cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg2 = cv2.createBackgroundSubtractorKNN()

while(1):
    ret,frame = cap.read()
    
    mask = fgbg.apply(frame)
    mask2 = fgbg2.apply(frame)
    mask2 = cv2.morphologyEx(mask2,cv2.MORPH_OPEN,kernel)

    cv2.imshow("Normal Video",frame)
    cv2.imshow("MOG2 Video",mask)
    cv2.imshow("KNN Video",mask2)

    k = cv2.waitKey(30) & 0xFF

    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()