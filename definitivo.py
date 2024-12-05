import serial
import time

# Configuración del puerto serie
port = "COM3"  # Cambia al puerto correcto
baud_rate = 9600  # Asegúrate de que coincida con la configuración de la balanza

def conectar_balanza():
    """Intenta conectar al puerto serie y retorna el objeto Serial."""
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Conectado a la balanza en el puerto {port}")
        return ser
    except serial.SerialException as e:
        print(f"Error al conectar con la balanza: {e}")
        return None

def enviar_comando(ser, comando):
    """Envía un comando a la balanza."""
    try:
        ser.write(comando.encode('utf-8'))  # Enviar el comando
        ser.flush()  # Asegurarse de que se envió
        time.sleep(0.5)  # Breve pausa para esperar la respuesta
        respuesta = ser.readline().decode('utf-8', errors='ignore').strip()
        print(f"Respuesta de la balanza: {respuesta}")
        return respuesta
    except Exception as e:
        print(f"Error al enviar el comando: {e}")
        return None

# Inicio del programa
serial_conn = conectar_balanza()
if serial_conn:
    # Ejemplo: Solicitar peso
    print("Solicitando peso...")
    enviar_comando(serial_conn, "S\r\n")
    
    # Esperar y leer datos continuamente (opcional)
    while True:
        try:
            raw_data = serial_conn.readline()
            if raw_data:
                decoded_data = raw_data.decode('utf-8', errors='ignore').strip()
                print(f"Peso detectado: {decoded_data}")
            else:
                print("Esperando datos...")
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nCerrando conexión con la balanza.")
            break
    serial_conn.close()
else:
    print("No se pudo conectar a la balanza.")
