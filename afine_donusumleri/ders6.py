import numpy as np
import cv2
from skimage.transform import AffineTransform, warp, resize, rescale

im = cv2.imread("res/orijinal/ornek_v1.jpg")

row,col,ch = im.shape

p1 = np.float32([[0,0],[col-1,0],[0,row-1]])
p2 = np.float32([[10,10],[col-50,20],[20,row-40]])

m = cv2.getAffineTransform(p1,p2)
im2 = cv2.warpAffine(im, m, (col,row))

cv2.imshow("affine resim",im2)

cv2.waitKey(0)
cv2.destroyAllWindows()
