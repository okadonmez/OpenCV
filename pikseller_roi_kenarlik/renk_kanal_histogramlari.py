import cv2
from matplotlib import pyplot as plt


img = cv2.imread("res/orijinal/ornek_v4.jpg")

b,g,r = cv2.split(img)

cv2.imshow("Normal",img)
cv2.imshow("Blue",b)
cv2.imshow("Green",g)
cv2.imshow("Red",r)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()