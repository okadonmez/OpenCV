import cv2
import matplotlib.pyplot as plt


resim = cv2.imread("res/orijinal/ornek_v1.jpg")

kirp = resim[127:255,127:255]

plt.subplot(121) #1 Satir, 2 sutundan olusacak ve bu 1.'si.
plt.imshow(resim)

plt.subplot(122) #1 Satir, 2 sutundan olusacak ve bu 2.'si.
plt.imshow(kirp)

plt.show()