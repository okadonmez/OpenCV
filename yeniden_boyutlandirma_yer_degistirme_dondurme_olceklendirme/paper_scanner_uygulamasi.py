import cv2
import numpy as np


img = cv2.imread("res/orijinal/ornek_v1.jpg")

rows,cols = img.shape[:2]

click_count = 0
a = []

dst_points = np.float32([
    [0,0],
    [cols-1,0],
    [0,rows-1],
    [cols-1,rows-1]
])

cv2.namedWindow("Resim",cv2.WINDOW_NORMAL)
cv2.namedWindow("Cikti",cv2.WINDOW_NORMAL)

def draw(event,x,y,flags,param):
    global click_count,a

    if click_count < 4:
        if event == cv2.EVENT_LBUTTONDBLCLK:
            click_count += 1
            a.append((x,y))
    else:
        src = np.float32([
            [a[0][0],a[0][1]],
            [a[1][0],a[1][1]],
            [a[2][0],a[2][1]],
            [a[3][0],a[3][1]]
        ])

        click_count = 0
        a = []

        M = cv2.getPerspectiveTransform(src,dst_points)
        img_output = cv2.warpPerspective(img,M,(cols,rows))
        cv2.imshow("Cikti",img_output)

    pass

cv2.setMouseCallback("Resim",draw)


while(1):
    cv2.imshow("Resim",img)
    
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()