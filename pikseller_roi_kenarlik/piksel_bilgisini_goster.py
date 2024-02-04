import cv2


resim = cv2.imread("res/orijinal/ornek_v1.jpg")

px = resim[100,100]

print("BGR: " + str(px))

px_blue = resim[100,100,0]
px_green = resim[100,100,1]
px_red = resim[100,100,2]

print("Blue: " + str(px_blue))
print("Green: " + str(px_green))
print("Red: " + str(px_red))

