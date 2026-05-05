import cv2

# Cargamos en una variable el modelo preentrenado
cascada_rostro = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error al detectar cámara")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al obtener los frames")
        break

    grises = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rostro = cascada_rostro.detectMultiScale(
        grises,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in rostro:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(frame, "Larper dentro", (x, y -10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow("Detector de caras", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

