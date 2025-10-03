import cv2
import datetime
import csv
import os

# Ruta absoluta de la carpeta donde está el script .py
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "asistencias.csv")

print(f"El archivo de asistencias se guardará en: {filename}")

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Cargar el clasificador de rostros de OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Crear archivo si no existe y escribir encabezados
if not os.path.isfile(filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")  
        writer.writerow(["Fecha", "Hora", "Estudiante"])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    fecha_actual = datetime.date.today().strftime("%Y-%m-%d")
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

    # Dibujar las caras detectadas
    for i, (x, y, w, h) in enumerate(faces):
        estudiante_id = f"Estudiante_{i+1}"
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, estudiante_id, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Registro de Asistencia", frame)

    # Guardar registros al presionar ESPACIO
    key = cv2.waitKey(1) & 0xFF
    if key == ord(" "):
        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")  # <-- usar punto y coma
            for i in range(len(faces)):
                estudiante_id = f"Estudiante_{i+1}"
                writer.writerow([fecha_actual, hora_actual, estudiante_id])
        print(f"{len(faces)} registros guardados en el archivo.")

    # Salir con "q"
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
