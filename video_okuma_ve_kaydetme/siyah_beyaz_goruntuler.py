import cv2
import numpy as np

sifir = np.zeros([100,100])
bir = np.ones([100,100])

cv2.namedWindow("Sifir",cv2.WINDOW_NORMAL) #Siyah
cv2.namedWindow("Bir",cv2.WINDOW_NORMAL) #Beyaz

print(sifir)
print("\n\n")
print(bir)

cv2.imshow("Sifir",sifir)
cv2.imshow("Bir",bir)

cv2.waitKey(0)

cv2.destroyAllWindows()