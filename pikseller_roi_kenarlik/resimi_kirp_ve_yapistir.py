import cv2
import matplotlib.pyplot as plt


resim = cv2.imread("res/orijinal/ornek_v1.jpg")

kirp = resim[100:300,100:300]

resim[0:200,0:200] = kirp

plt.subplot(121)
plt.imshow(resim)

plt.subplot(122)
plt.imshow(kirp)

plt.show()