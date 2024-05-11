import numpy as np
import cv2
from skimage.transform import AffineTransform, warp, resize, rescale

im = cv2.imread("res/orijinal/ornek_v1.jpg")

im1 = rescale(im, 1.2, order=0)
im2 = rescale(im, 1.2, order=1)
im3 = rescale(im, 1.2, order=2)
im4 = rescale(im, 1.2, order=3)

#interpolasyon yapamazsa buyuturken veya kuculturken resimde kayiplar olur renk gibi vs. ozellikler bulanik olur

cv2.imshow("Orijinal Resim",im)
cv2.imshow("Order 1 Resim",im1)
cv2.imshow("Order 2 Resim",im2)
cv2.imshow("Order 3 Resim",im3)
cv2.imshow("Order 4 Resim",im4)

cv2.waitKey(0)
cv2.destroyAllWindows()