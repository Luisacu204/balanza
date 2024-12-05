import serial

# Configuración del puerto serie (ajusta según tu configuración)
ser = serial.Serial('COM4', 9600, timeout=1)  # Reemplaza 'COM3' por el puerto correcto

def obtener_peso():
    """Envía un comando a la balanza y devuelve el peso."""
    # Enviar comando para solicitar el peso (ejemplo)
    ser.write(b'W\r')  # Reemplaza 'W\r' por el comando correcto para tu balanza

    # Leer los datos
    data = ser.readline().decode('ascii').strip()

    # Procesar los datos (ejemplo)
    try:
        peso = float(data)
        return peso
    except ValueError:
        print("Error al convertir los datos a un número.")
        return None

# Obtener el peso
peso = obtener_peso()

if peso is not None:
    print("El peso es:", peso)
else:
    print("No se pudo obtener el peso.")

# Cerrar el puerto serial
ser.close()