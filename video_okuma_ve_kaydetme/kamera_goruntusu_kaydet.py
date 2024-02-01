import cv2

cam = cv2.VideoCapture(0)

#fourrc = cv2.VideoWriter_fourcc('M','J','P','G') #Bu kod, video sıkıştırma formatını belirtir ve bu sayede video dosyasının hangi codec (sıkıştırma/decompression) kullanılarak yazılacağını belirler. Bunlari yaptigimizda ".mp4" formatinda olur.
fourrc = cv2.VideoWriter_fourcc(*'XVID') #Windows'ta en tutarli olani * icin olanidir. Bu da boyutu biraz daha azaltir.

out = cv2.VideoWriter("res/degistirilmis/kamera_goruntusu_kaydet.avi",fourrc,30.0,(640,480))

while cam.isOpened():
    ret, frame = cam.read()

    if not ret:
        print("Kameradan  goruntu okunamiyor.")
        break

    out.write(frame)

    cv2.imshow("Kamera",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Videodan ayrildiniz.")
        break

cam.release()
out.release()
cv2.destroyAllWindows()