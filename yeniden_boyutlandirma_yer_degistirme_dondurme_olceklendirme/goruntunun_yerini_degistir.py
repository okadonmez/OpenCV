import cv2
import numpy as np


img = cv2.imread("res/orijinal/ornek_v1.jpg")

rows,cols = img.shape[:2]

translation_matrix = np.float32([
    [1,0,25], #25 x uzerinde kac piksel kaydirilacagini belirtir.
    [0,1,25]  #25 y uzerinde kac piksel kaydirilacagini belirtir.
])

img_translation = cv2.warpAffine(img,translation_matrix,(cols+50,rows+50))

cv2.imshow("Resim",img)
cv2.imshow("Resim Translation",img_translation)

cv2.waitKey()
cv2.destroyAllWindows()