# Forma simple de abrir cámara

import cv2

captura = cv2.VideoCapture(0)

if not captura.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

while True:
    ret, frame = captura.read()
    if not ret:
        print("Error: no se pude leer el contenido de la cámara")
        break

    cv2.imshow("Camara en vivo", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows() 

