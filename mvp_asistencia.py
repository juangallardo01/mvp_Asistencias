import cv2
from datetime import datetime, timedelta
import csv
import os

# Guardar el archivo en la misma carpeta del script
archivo = os.path.join(os.path.dirname(__file__), "asistencias.csv")

# Si no existe el archivo, crear encabezado con delimitador ";"
if not os.path.exists(archivo):
    with open(archivo, mode="w", newline="") as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(["Fecha", "Hora", "Estudiante"])

# Clasificador de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

student_count = 0
ultimo_registro = datetime.min  # Control del tiempo

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo acceder a la cámara")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Verificar si pasaron al menos 10 segundos desde el último registro
        if datetime.now() - ultimo_registro > timedelta(seconds=10):
            student_count += 1
            nombre = f"Estudiante_{student_count}"

            # Guardar en CSV con ";" como separador
            fecha = datetime.now().strftime("%Y-%m-%d")
            hora = datetime.now().strftime("%H:%M:%S")
            with open(archivo, mode="a", newline="") as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow([fecha, hora, nombre])

            print(f"Asistencia registrada: {nombre} - {fecha} {hora}")
            ultimo_registro = datetime.now()
        else:
            nombre = "Esperando..."

        # Dibujar rectángulo y nombre en pantalla
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, nombre, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    cv2.imshow('Prototipo Asistencia', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
