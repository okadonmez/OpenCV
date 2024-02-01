import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

pts = np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)

print(pts)

pts2 = pts.reshape(-1,1,2)

print(pts2)

cv2.polylines(img,[pts],False,(255,255,255),3)

pts = np.array([[150,300],[400,200],[75,60],[250,350]],np.int32)

pts2 = pts.reshape(-1,1,2)

cv2.polylines(img,[pts],True,(0,255,255),3)

cv2.imshow("Resim",img)

cv2.waitKey(0)

cv2.destroyAllWindows()