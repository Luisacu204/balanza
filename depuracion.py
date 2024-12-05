import serial
import time

# Configuración del puerto serie
port = "COM3"  # Cambiar al puerto correcto
baud_rate = 9600  # Ajustar según la configuración de la balanza

def conectar_balanza():
    """Intenta conectar al puerto serie y retorna el objeto Serial."""
    try:
        ser = serial.Serial(port, baud_rate, timeout=5)
        print(f"Conectado a la balanza en el puerto {port}")
        return ser
    except serial.SerialException as e:
        print(f"Error al conectar con la balanza: {e}")
        return None

def enviar_comando_inicial(ser):
    """Envía un comando inicial para activar la balanza, si es necesario."""
    try:
        # Reemplaza 'COMANDO' con el comando correcto según el manual de la balanza
        comando = b'\r\n'  # Ejemplo: comando para iniciar transmisión
        ser.write(comando)
        print("Comando inicial enviado.")
    except Exception as e:
        print(f"Error al enviar comando inicial: {e}")

def leer_datos(ser):
    """Lee y procesa datos del puerto serie."""
    try:
        while True:
            raw_data = ser.readline()  # Leer línea del puerto serie
            print(f"Datos crudos: {raw_data}")  # Mostrar datos crudos (bytes)

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
            time.sleep(0.5)  # Pausa breve
    except KeyboardInterrupt:
        print("\nCerrando el programa.")
    finally:
        ser.close()

# Inicio del programa
serial_conn = conectar_balanza()
if serial_conn:
    enviar_comando_inicial(serial_conn)
    print("Esperando datos de la balanza...")
    leer_datos(serial_conn)
else:
    print("No se pudo establecer conexión con la balanza.")
