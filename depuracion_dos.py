# import serial

# port = "COM3"
# baud_rate = 9600

# try:
#     with serial.Serial(port, baud_rate, timeout=10) as ser:
#         print(f"Conectado a la balanza en el puerto {port}")

#         # Si necesitas enviar un comando inicial, descomenta:
#         # ser.write(b'\r\n')

#         while True:
#             raw_data = ser.readline()
#             print(f"Datos crudos: {raw_data}")  # Depuración de datos sin procesar

#             if raw_data:
#                 try:
#                     decoded_data = raw_data.decode('utf-8', errors='ignore').strip()
#                     if decoded_data:  # Solo muestra si no está vacío
#                         print(f"Peso detectado: {decoded_data}")
#                 except UnicodeDecodeError:
#                     print(f"Error al decodificar: {raw_data}")
#             else:
#                 print("Sin datos... esperando entrada.")
# except serial.SerialException as e:
#     print(f"Error al conectar con la balanza: {e}")
# except KeyboardInterrupt:
#     print("\nCerrando el programa.")

import serial
import time

# Configuración del puerto serie
port = "COM3"  # Ajustar al puerto correcto
baud_rate = 9600  # Cambiar según la configuración de la balanza

def conectar_balanza():
    """Intenta conectar al puerto serie y retorna el objeto Serial."""
    try:
        ser = serial.Serial(port, baud_rate, timeout=5)
        print(f"Conectado a la balanza en el puerto {port}")
        return ser
    except serial.SerialException as e:
        print(f"Error al conectar con la balanza: {e}")
        return None

def leer_datos(ser):
    """Lee y procesa datos del puerto serie."""
    try:
        while True:
            raw_data = ser.readline()  # Leer línea del puerto serie
            if raw_data:
                try:
                    # Decodificar datos
                    decoded_data = raw_data.decode('utf-8', errors='ignore').strip()
                    if decoded_data:  # Si los datos no están vacíos
                        print(f"Peso detectado: {decoded_data}")
                    else:
                        print("Datos decodificados vacíos, esperando...")
                except UnicodeDecodeError:
                    print(f"Error al decodificar datos: {raw_data}")
            else:
                print("Sin datos, esperando entrada...")
            time.sleep(0.5)  # Pequeña pausa para evitar saturar el puerto
    except KeyboardInterrupt:
        print("\nCerrando el programa.")
    finally:
        ser.close()

# Inicio del programa
serial_conn = conectar_balanza()
if serial_conn:
    print("Esperando datos de la balanza...")
    leer_datos(serial_conn)
else:
    print("No se pudo establecer conexión con la balanza.")

