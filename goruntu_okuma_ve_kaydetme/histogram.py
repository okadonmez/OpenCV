import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("ders/polen.png",0)

hist = cv2.calcHist(img,[0],None,[255],[0,255])


cv2.imshow("ders/polen.png",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#equal = equallisthist7



plt.plot(hist)
plt.show()
