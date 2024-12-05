import serial

# Configuración del puerto
port = "COM3"  # Cambiar al puerto correcto
baud_rate = 9600  # Ajustar según las especificaciones de la balanza

try:
    with serial.Serial(port, baud_rate, timeout=1) as ser:
        print(f"Conectado a la balanza en el puerto {port}")

        while True:
            # Leer datos crudos de la balanza
            raw_data = ser.readline()
            
            if raw_data:  # Si se reciben datos
                try:
                    # Intentar decodificar los datos
                    decoded_data = raw_data.decode('utf-8').strip()
                    
                    if decoded_data:  # Si no está vacío
                        print(f"Peso detectado: {decoded_data}")
                except UnicodeDecodeError:
                    print(f"Error de decodificación: {raw_data}")
except serial.SerialException as e:
    print(f"Error al conectar con la balanza: {e}")
except KeyboardInterrupt:
    print("\nCerrando el programa.")
