import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error al detectar la cámara")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al recibir lectura en la camara")
        break

    grises = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.rectangle(frame, (160, 100), (460,400), (255, 0, 0), 3)
    cv2.putText(frame, "Larper dentro!", (190, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))


    cv2.imshow("Camara normal", frame)
    cv2.imshow("Camara con color", grises)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()