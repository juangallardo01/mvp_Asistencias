# MVP Asistencia con Detección Facial (Simulación)

Este proyecto es un **prototipo de reingeniería de procesos** aplicado a la toma de asistencia en la facultad.  
En lugar de marcar asistencia de forma manual o con QR como se hace actualmente, se utiliza la cámara del dispositivo para **detectar rostros** y registrar automáticamente la asistencia en un archivo CSV.

Este MVP **no realiza reconocimiento biométrico real**. Cada rostro detectado se etiqueta de forma genérica como `Estudiante_X`, donde X representa un contador autoincremental.

Forma de uso:
  - Ejecutar archivo .py
  - Uibcar el rostro del alumno en la pantalla y en consola aparecerá el mensaje de que fue tomada la asistencia correctamente
  - Antes de detectar otro rostro, el programa espera 10 segundos para evitar que detecte el mismo rostro dos veces.
  - Pasados 10 segundos podemos detectar el siguiente rostro y asi de manera consecutiva.
  - Para finalizar la ejecucion, en la ventana de la camara apretamos la tecla Q.

Una vez finalizada la ejecucion del programa vamos a obtener en nustra carpeta donde guardamos el archivo .py un archivo csv con los datos de las astistencias, que podemos abrir mediante excel.


