import cv2

resim = cv2.imread("res/orijinal/ornek_v1.jpg",0)

cv2.imshow("Resim Penceresi", resim)

k = cv2.waitKey(0)

if k == 27:
    print("ESC tusuna basildi, resim kayit edilmedi.")
elif k == ord("q"):
    print("q tusuna basildi, resim kayit edildi.")
    cv2.imwrite("res/degistirilmis/ornek_v1_gri.jpg",resim)

cv2.destroyAllWindow()