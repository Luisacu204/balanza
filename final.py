import serial
import time

# Configuración del puerto serial (ajusta según tu puerto)
PUERTO_SERIAL = 'COM6'  # Cambia esto a tu puerto, por ejemplo, '/dev/ttyUSB0' en Linux
BAUD_RATE = 9600        # Asegúrate de que esta es la tasa de baudios correcta para tu balanza

try:
    # Abre el puerto serial
    ser = serial.Serial(PUERTO_SERIAL, BAUD_RATE, timeout=1)
    print(f"Conexión establecida con la balanza en el puerto {PUERTO_SERIAL}")
except serial.SerialException as e:
    print(f"Error al abrir el puerto: {e}")
    exit()

# Intentar leer datos
while True:
    try:
        if ser.in_waiting > 0:  # Si hay datos en el buffer de entrada
            datos_brutos = ser.read(ser.in_waiting)  # Lee todos los datos disponibles
            print(f"Datos crudos: {datos_brutos}")
            # Intentamos decodificar los bytes de forma más general (latin-1)
            datos_decodificados = datos_brutos.decode('latin-1', errors='ignore')
            print(f"Datos decodificados: {datos_decodificados}")
        else:
            print("Esperando datos...")
    except Exception as e:
        print(f"Error al procesar la respuesta: {e}")
    
    time.sleep(1)  # Pausa de 1 segundo para evitar leer constantemente sin pausa

# Este codigo funciona bien... guardar en el repositorio y modificar para filtrar bien. 