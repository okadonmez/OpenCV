import cv2


resim = cv2.imread("res/orijinal/ornek_v1.jpg")


px = resim.item(100,100,0)

print("Blue: " + str(px))

px = resim.item(100,100,1)

print("Green: " + str(px))

px = resim.item(100,100,2)

print("Red: " + str(px))


resim.itemset((100,100,0),50)
px = resim.item(100,100,0)

print("Yeni Blue: " + str(px))