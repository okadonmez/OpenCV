import cv2


resim = cv2.imread("res/orijinal/ornek_v1.jpg")

print("Resimin Boyutu: " + str(resim.shape))
print("Resimin Piksel Sayisi (Yukseklik x Genislik x 3): " + str(resim.size))
print("Resimin Verilerinin Turu: " + str(resim.dtype))