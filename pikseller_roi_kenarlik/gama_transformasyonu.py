import cv2
import numpy as np

image = cv2.imread("res/orijinal/ornek_v4.jpg")

print(image.dtype)

img_neg = 255 - image

for gamma in [0.1, 0.5, 0.4, 0.6, 1, 1.5, 2]:
    gamma_transformation = np.array(255 * (image / 255) ** gamma, dtype="uint8")

    cv2.imwrite("res/degistirilmis/ornek_v4_gama" + str(gamma) + ".jpg", gamma_transformation)
    cv2.imshow("Gamma Resim", gamma_transformation)

cv2.imshow("Orijinal Resim", image)

cv2.waitKey(0)
cv2.destroyAllWindows()