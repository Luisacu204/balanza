import serial

port = "COM3"  # Cambia al puerto correcto
baud_rate = 9600  # Cambia según la configuración de la balanza

try:
    with serial.Serial(port, baud_rate, timeout=1) as ser:
        print(f"Conectado a la balanza en el puerto {port}")

        while True:
            raw_data = ser.readline()
            if raw_data:
                try:
                    decoded_data = raw_data.decode('utf-8').strip()
                    print(f"Peso recibido: {decoded_data}")
                except UnicodeDecodeError:
                    print(f"Error de decodificación: {raw_data}")
except serial.SerialException as e:
    print(f"Error al conectar con la balanza: {e}")
except KeyboardInterrupt:
    print("\nCerrando el programa.")
