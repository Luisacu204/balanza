import serial
import time

# Configuración del puerto serie
port = "COM3"  # Cambia al puerto correcto
baud_rate = 9600  # Velocidad de baudios según la configuración de la balanza

def conectar_balanza():
    """Intenta conectar al puerto serie y retorna el objeto Serial."""
    try:
        ser = serial.Serial(port, baud_rate, bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
        print(f"Conectado a la balanza en el puerto {port}")
        return ser
    except serial.SerialException as e:
        print(f"Error al conectar con la balanza: {e}")
        return None

def solicitar_peso(ser):
    """Envía el comando para solicitar el peso y lee la respuesta."""
    try:
        comando = 'S\r\n'  # Comando para solicitar el peso
        ser.write(comando.encode('utf-8'))  # Enviar el comando
        time.sleep(0.5)  # Esperar una respuesta
        respuesta = ser.readline().decode('utf-8').strip()  # Leer y decodificar la respuesta
        if respuesta:
            print(f"Peso detectado: {respuesta}")
        else:
            print("No se recibió respuesta de la balanza.")
    except Exception as e:
        print(f"Error al solicitar el peso: {e}")

# Inicio del programa
if __name__ == "__main__":
    balanza = conectar_balanza()
    if balanza:
        while True:
            solicitar_peso(balanza)
            time.sleep(1)  # Esperar antes de la siguiente solicitud
    else:
        print("No se pudo establecer conexión con la balanza.")
