import serial
import time

port = "COM3"  
baud_rate = 9600  

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
        comando = 'S\r\n'
        ser.write(comando.encode('utf-8')) # Aqui es ASCII segun sea...
        time.sleep(0.5)
        respuesta = ser.readline().decode('utf-8').strip()
        if respuesta:
            print(f"Peso detectado: {respuesta}")
        else:
            print("No se recibió respuesta de la balanza.")
    except Exception as e:
        print(f"Error al solicitar el peso: {e}")

if __name__ == "__main__":
    balanza = conectar_balanza()
    if balanza:
        while True:
            solicitar_peso(balanza)
            time.sleep(1)  
    else:
        print("No se pudo establecer conexión con la balanza.")
