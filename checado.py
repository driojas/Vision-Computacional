import cv2
import numpy as np

camara = cv2.VideoCapture(0)

while True:
    ret, frame = camara.read()

    if not ret:
        break

    # Separo los canales de color
    azul = frame[:, :, 0]
    verde = frame[:, :, 1]
    rojo = frame[:, :, 2]

    #promedio
    promedio = (azul.astype(float) + verde + rojo) / 3
    blanco_negro = np.where(promedio >= 127, 255, 0).astype(np.uint8)

    # Muestra video
    cv2.imshow("Webcam - Blanco y Negro", blanco_negro)

    # Presionar Q para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara
camara.release()
cv2.destroyAllWindows()