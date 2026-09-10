import cv2

camara = cv2.VideoCapture(0) # Abrir la webcam

while True: #para siempre leer frames 
    ret, frame = camara.read() #devuelve true o false en si obtuvo el frame o no

    if not ret:
        break

    # Convertir a escala de grises primero
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    # Convertir a blanco y negro
    _, blanco_negro = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY) #127 mitad de 255, binary 2 resultados B o N. 
    #trheshold devuelve el 127 y la imagen pero solo nos intereas la imagen
    # Mostrar el video
    cv2.imshow("Webcam - Blanco y Negro", blanco_negro)

    # Presionar Q para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara
camara.release()
cv2.destroyAllWindows()
