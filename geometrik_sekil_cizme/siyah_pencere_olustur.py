import cv2
import numpy as np


#img = np.zeros((512,512)) #Tek boyutlu siyah siyah bir gorsel olusturur. Tek duzlemlidir. Sadece siyah veya beyaz olabilir.
#img = np.zeros((512,512,3)) #3 Boyutlu RGB veya BGR formatinda olabilir artik. Cunku 3 renk uzayina sahip simdi. Bu sekilde kalirsa default degerler alir.
img = np.zeros((512,512,3),np.uint8) #Pozitif int sayilar kullanacagimizi belirttik.

cv2.imshow("Resim",img)

cv2.waitKey(0)

cv2.destroyAllWindows()