import cv2
import numpy as np


x = np.uint8([250])
y = np.uint8([10])

sonuc1 = x + y

print(sonuc1) #260 % 256 = 4.

sonuc2 = cv2.add(x,y)

print(sonuc2) #max deger 255 olur toplami bunu gecemez.