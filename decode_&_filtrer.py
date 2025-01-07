import serial
import time
import re
import keyboard  # Asegúrate de instalar esta biblioteca con `pip install keyboard`


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

print("Presiona la tecla 'p' para obtener el peso.")

# Bucle principal
while True:
    try:
        if keyboard.is_pressed('p'):  # Detecta si se presiona la tecla 'p'
            # Vacía el búfer de entrada para asegurarte de obtener datos nuevos
            ser.reset_input_buffer()

            # Espera un breve momento para que lleguen los datos más recientes
            time.sleep(0.1)

            if ser.in_waiting > 0:
                datos_brutos = ser.read(ser.in_waiting)
                datos_decodificados = datos_brutos.decode('latin-1', errors='ignore')

                # Expresión regular para encontrar los 4 dígitos después del primer "0"
                patron = r"0(\d{4})"
                coincidencia = re.search(patron, datos_decodificados)

                if coincidencia:
                    four_digits = coincidencia.group(1)
                    cuatro_digitos = int(four_digits)
                    primer_digito = four_digits[0]

                    if primer_digito == '0':    
                        gramos = cuatro_digitos / 1000
                        print(f"Equivalente en gramos: {gramos:.3f} gr")  # Formato con 3 decimales
                    else:
                        kilogramos = cuatro_digitos / 1000  # Convertimos a kilogramos para mantener la consistencia
                        print(f"Equivalente en kilogramos: {kilogramos:.3f} kg")  # Formato con 3 decimales
                else:
                    print("No se encontraron los 4 dígitos después del primer 0")
            else:
                print("No hay datos disponibles en el puerto.")

            time.sleep(0.5)  # Agrega un pequeño retardo para evitar múltiples lecturas al presionar la tecla
    except Exception as e:
        print(f"Error al procesar la respuesta: {e}")

    time.sleep(0.1)  # Retardo breve para no saturar el procesador
