import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

ruta_modelo = '/home/ferran/Documentos/python-projects/detector_somnolencia/hand_landmarker.task'
opciones = vision.HandLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path=ruta_modelo),
    min_hand_detection_confidence=0.5,
    num_hands=1
)
detector = vision.HandLandmarker.create_from_options(opciones)


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error al abrir cámara")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al obtener fotogramas")
        break

    frame = cv2.flip(frame, 1)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

    resultados = detector.detect(mp_image)

    if resultados.hand_landmarks:
        for mano in resultados.hand_landmarks:
            alto, ancho, _ = frame.shape

            punto_8 =mano[8]

            x = int(punto_8.x * ancho)
            y = int(punto_8.y * alto)
        
        mitad_pantalla = ancho // 2

        if x < mitad_pantalla:
            color = (0, 0, 255)
            cv2.putText(frame, "Izquierda", (x-75, y-20), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
        else: 
            color = (0, 255, 0)
            cv2.putText(frame, "Derecha", (x-75, y-20), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)


    cv2.imshow("Camara en vivo", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Cerrando el programa")
        break

cap.release()
cv2.destroyAllWindows()